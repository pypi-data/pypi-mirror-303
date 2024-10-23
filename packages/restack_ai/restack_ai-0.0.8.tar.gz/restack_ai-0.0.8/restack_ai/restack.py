import os
import asyncio
from pydantic import BaseModel
from typing import Optional, Dict, Any, List, final
from temporalio.client import Client, ScheduleSpec
from temporalio.worker import Worker
from .observability import logger

class CloudConnectionOptions(BaseModel):
    engine_id: str
    api_key: str
    address: Optional[str] = "localhost:7233"
    temporal_namespace: Optional[str] = "default"

class ServiceOptions(BaseModel):
    rate_limit: Optional[int] = 100000
    max_concurrent_workflow_runs: Optional[int] = 3000
    max_concurrent_function_runs: Optional[int] = 1000

class ServiceInput(BaseModel):
    workflows_path: Optional[str]
    functions: Optional[List[Any]]
    options: Optional[ServiceOptions] = ServiceOptions()

class Restack:
    def __init__(self, options: Optional[CloudConnectionOptions] = None):
        self.client = None
        self.options = options
        logger.debug("Restack instance initialized", meta={"options": options})

    def get_connection_options(self) -> Dict[str, Any]:
        target_host = self.options.address if self.options else 'localhost:7233'
        engine_id = self.options.engine_id if self.options else 'local'
        options = {
            "target_host": target_host,
            "metadata": {
                "restack-engineId": engine_id,
            }
        }
        if self.options and self.options.api_key:
            options["tls"] = not target_host.startswith("localhost")
            options["api_key"] = self.options.api_key
        return options
    
    async def connect(self, connection_options: Optional[CloudConnectionOptions] = None):
        if self.client:
            logger.info("Reusing existing client connection.")
            return
        try:
            self.client = await self.create_client(connection_options)
            logger.info("Connected to Restack Engine.")
        except Exception as e:
            logger.error("Failed to connect to Restack Engine", meta={"error": str(e)})
            raise e

    async def create_client(self, connection_options: Optional[CloudConnectionOptions] = None) -> Client:
        connect_options = connection_options or self.get_connection_options()
        namespace = self.options.temporal_namespace if self.options else 'default'

        return await Client.connect(
            connect_options['target_host'],
            namespace=namespace
        )

    async def create_service(self, service_input: ServiceInput) -> Worker:
        try:
            logger.info("Starting service...")
            client = await self.create_client()
            engine_id = self.get_connection_options()['metadata']['restack-engineId']

            service = Worker(
                identity=f"{engine_id}-{os.getpid()}@{os.uname().nodename}",
                client=client,
                task_queue='restack',
                workflows=service_input['workflows'],
                activities=service_input['functions'],
            )
            logger.info("Service created successfully.")
            return service
        except Exception as e:
            logger.error("Failed to start service", meta={"error": str(e)})
            raise e

    async def run_service(self, service: Worker):
        try:
            logger.info("Starting service...")
            await service.run()
            logger.info("Service is running.")
        except asyncio.CancelledError or KeyboardInterrupt:
            logger.info("Service was cancelled. Shutting down gracefully...")
        except Exception as e:
            logger.error("Failed to run service", meta={"error": e})
            raise e
        finally:
            logger.info("Service shutdown complete.")

    async def start_service(self, service_input: ServiceInput):
        service = await self.create_service(service_input)
        await self.run_service(service)

    async def schedule_workflow(self, workflow_name: str, workflow_id: str, input: Optional[Dict[str, Any]] = None, schedule: Optional[ScheduleSpec] = None, task_queue: Optional[str] = 'restack') -> str:
        await self.connect()
        if self.client:
            try:
                connection_options = self.get_connection_options()
                engine_id = connection_options['metadata']['restack-engineId']

                if not schedule:
                    handle = await self.client.start_workflow(
                        workflow_name,
                        args=[input] if input else [],
                        id=f"{engine_id}-{workflow_id}",
                        memo={'engineId': engine_id},
                        search_attributes={'engineId': [engine_id]},
                        task_queue=task_queue,
                    )
                    logger.info("Workflow started immediately with runId", meta={"runId": handle.first_execution_run_id})
                    return handle.first_execution_run_id
                else:
                    scheduled = await self.client.create_schedule(
                        id=f"{engine_id}-{workflow_id}",
                        schedule=schedule,
                        action=Client.ScheduleActionStartWorkflow(
                            workflow_name,
                            args=[input] if input else [],
                        ),
                        memo={'engineId': engine_id},
                        search_attributes={'engineId': [engine_id]},
                        task_queue=task_queue,
                    )
                    logger.info("Workflow scheduled with scheduleId", meta={"scheduleId": scheduled.schedule_id})
                    return scheduled.schedule_id
            except Exception as e:
                logger.error("Failed to start or schedule workflow", meta={"error": str(e)})
                raise e
        else:
            raise Exception("Workflow result not retrieved due to failed connection.")

    async def get_workflow_handle(self, workflow_id: str, run_id: str):
        await self.connect()
        if self.client:
            try:
                connection_options = self.get_connection_options()
                engine_id = connection_options['metadata']['restack-engineId']
                return self.client.get_workflow_handle(f"{engine_id}-{workflow_id}", run_id=run_id)
            except Exception as e:
                logger.error("Failed to get workflow result", meta={"error": str(e)})
                raise e
        else:
            raise Exception("Workflow result not retrieved due to failed connection.")

    async def get_workflow_result(self, workflow_id: str, run_id: str) -> Any:
        handle = await self.get_workflow_handle(workflow_id, run_id)
        return await handle.result()

    async def send_workflow_event(self, event: Dict[str, Any], workflow: Dict[str, str]):
        if self.client:
            try:
                workflow_id, run_id = workflow['workflowId'], workflow['runId']
                name, input = event['name'], event['input']
                handle = self.client.get_workflow_handle(workflow_id, run_id)
                return await handle.signal(name, input)
            except Exception as e:
                logger.error("Failed to send workflow event", meta={"error": str(e)})
                raise e
        else:
            raise Exception("Workflow result not retrieved due to failed connection.")