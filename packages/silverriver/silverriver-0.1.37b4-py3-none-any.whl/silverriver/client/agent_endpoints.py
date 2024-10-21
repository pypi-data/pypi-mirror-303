import pydantic

from silverriver.client.endpoint import Endpoint
from silverriver.interfaces import AgentAction, AgentActionRequest, SupportedModes


class SotaAgentConfig(pydantic.BaseModel, extra="forbid"):
    max_retry: int = 4
    mode: SupportedModes = SupportedModes.PRIME
    use_multi_actions: bool = True


class SotaAgentEndpoints:
    PREFIX = "/api/v1/sota_agent"

    GET_ACTION = Endpoint(prefix=PREFIX, path="/get_action", method="POST", response_model=AgentAction,
                          request_model=AgentActionRequest)
    CLOSE = Endpoint(prefix=PREFIX, path="/close", method="POST", response_model=None, request_model=None)
