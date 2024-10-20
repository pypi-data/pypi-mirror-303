from temporalio import activity
from temporalio.exceptions import ApplicationError

# Exported functions and classes
FunctionFailure = ApplicationError
log = activity.logger
function_info = activity.info
heartbeat = activity.heartbeat
function = activity
sleep = activity.sleep

__all__ = [
    'FunctionFailure',
    'log',
    'function_info',
    'heartbeat',
    'sleep'
]

def current_workflow():
    return activity.Context.current().info