from pydantic import BaseModel
from typing import Any, Dict, Optional, TypeVar, Callable, Awaitable
from temporalio import workflow

# Define the UpdateDefinition equivalent
T = TypeVar('T')
Args = TypeVar('Args')

class UpdateDefinition(BaseModel):
    name: str

def define_event(name: str) -> UpdateDefinition:
    return UpdateDefinition(name=name)

def on_event(definition: UpdateDefinition, handler: Callable[[Args], Awaitable[T] | T], options: Optional[Dict[str, Any]] = None):
    # Simulate setting a handler for the event
    workflow.set_handler(definition.name, handler, options)

class WorkflowEvent(BaseModel):
    name: str
    input: Optional[Dict[str, Any]] = None

class SendWorkflowEvent(BaseModel):
    event: WorkflowEvent
    workflow: Optional[str] = None  # Adjust type as needed for workflow execution info