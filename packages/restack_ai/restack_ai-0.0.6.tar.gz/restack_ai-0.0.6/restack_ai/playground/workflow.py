from pydantic import BaseModel
from temporalio import workflow, activity

class PlaygroundInput(BaseModel):
    function_name: str
    task_queue: str
    input: any

@activity.defn
async def schedule_activity(function_name: str, input: list, task_queue: str):
    # Simulate scheduling an activity
    return f"Activity {function_name} executed with input {input} on task queue {task_queue}"

@workflow.defn
class PlaygroundWorkflow:
    @workflow.run
    async def run(self, params: PlaygroundInput):
        result = await schedule_activity(
            params.function_name,
            [params.input],
            params.task_queue
        )
        return result