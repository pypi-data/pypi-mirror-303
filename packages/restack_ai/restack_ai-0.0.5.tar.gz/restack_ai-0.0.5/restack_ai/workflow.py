from temporalio import workflow as temporal_workflow

# Exported functions and classes
log = temporal_workflow.logger
get_external_workflow_handle = temporal_workflow.get_external_workflow_handle
workflow_info = temporal_workflow.info
continue_as_new = temporal_workflow.continue_as_new
condition = temporal_workflow.condition

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
# Create an instance of Workflow to be used as `workflow`
workflow = Workflow()