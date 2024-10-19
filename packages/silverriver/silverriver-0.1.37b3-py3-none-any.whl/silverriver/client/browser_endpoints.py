import pydantic

from silverriver.client.endpoint import Endpoint
from silverriver.interfaces import AgentAction, SetupInput, SubTransition


class RemoteSetupOutput(pydantic.BaseModel):
    init_acts: tuple[AgentAction, ...] = tuple()
    exec_context_params: dict = pydantic.Field(default_factory=dict)


class BrowserEndpoints:
    PREFIX = "/api/v1/browser"

    SETUP = Endpoint(prefix=PREFIX, path="/setup", method="POST", response_model=RemoteSetupOutput, request_model=SetupInput)
    INTERNAL_STEP = Endpoint(prefix=PREFIX, path="/internal_step", method="POST", response_model=SubTransition, request_model=AgentAction)
    CLOSE = Endpoint(prefix=PREFIX, path="/close", method="POST", response_model=None, request_model=None)
