from typing import Any, Dict, Optional
from temporalio import workflow as temporal_workflow

# Exported functions and classes
log = temporal_workflow.logger
get_external_workflow_handle = temporal_workflow.get_external_workflow_handle
workflow_info = temporal_workflow.info
continue_as_new = temporal_workflow.continue_as_new
condition = temporal_workflow.wait_condition

__all__ = [
    'log',
    'get_external_workflow_handle',
    'workflow_info',
    'continue_as_new',
    'condition'
]

class Workflow:
    def defn(self, *args, **kwargs):
        return temporal_workflow.defn(*args, **kwargs)
    def run(self, fn):
        return temporal_workflow.run(fn)
    async def step(self, activity, *args, **kwargs):
        return await temporal_workflow.execute_activity(activity, *args, **kwargs)
    async def child_start(self, workflow_func, input: Optional[Dict[str, Any]] = None, task_queue: Optional[str] = 'restack', options = {}):
        engine_id = self.get_engine_id_from_client()
        prefixed_options = {
            **options,
            'args': [input] if input else [],
            'id': self.add_engine_id_prefix(engine_id, options.get('workflow_id', 'default_id')),
            'memo': {'engineId': engine_id},
            'search_attributes': {
                'engine_id': [engine_id],
            },
            'task_queue': task_queue,
        }
        return await temporal_workflow.start_child_workflow(workflow_func, prefixed_options)

    async def child_execute(self, workflow_func, input: Optional[Dict[str, Any]] = None, task_queue: Optional[str] = 'restack', options = {}):
        engine_id = self.get_engine_id_from_client()
        prefixed_options = {
            **options,
            'args':[input] if input else [],
            'id': self.add_engine_id_prefix(engine_id, options['workflow_id']),
            'memo':{'engineId': engine_id},
            'search_attributes': {
                'engine_id': [engine_id],
            },
            'task_queue': task_queue,
        }
        return await temporal_workflow.execute_child_workflow(workflow_func, prefixed_options)

    def get_engine_id_from_client(self):
        # Implement this method to retrieve the engine ID from the client
        pass

    def add_engine_id_prefix(self, engine_id, workflow_id):
        # Implement this method to add the engine ID prefix to the workflow ID
        return f"{engine_id}-{workflow_id}"
# Create an instance of Workflow to be used as `workflow`
workflow = Workflow()
