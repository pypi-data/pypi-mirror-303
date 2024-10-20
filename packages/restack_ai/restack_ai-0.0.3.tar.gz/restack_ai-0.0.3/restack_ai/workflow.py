from temporalio import workflow as temporal_workflow


class Workflow:
    def defn(self, *args, **kwargs):
        return temporal_workflow.defn(*args, **kwargs)
    def run(self, fn):
        return temporal_workflow.run(fn)
    def signal(self, fn):
        return temporal_workflow.signal(fn)
    def query(self, fn):
        return temporal_workflow.query(fn)
    def sleep(self, seconds):
        return temporal_workflow.sleep(seconds)
    async def step(self, activity, *args, **kwargs):
        return await temporal_workflow.execute_activity(activity, *args, **kwargs)
# Create an instance of Workflow to be used as `workflow`
workflow = Workflow()