from enum import StrEnum

import pydantic

from silverriver.interfaces.data_models import Observation


class SupportedModes(StrEnum):
    FLASH = "flash"  # Typically faster, but less reliable in planning
    PRIME = "prime"  # Flagship mode, used for the most reliable results


class SubTransition(pydantic.BaseModel, extra="forbid"):
    # obs is purposely different from observation to ensure the two Transitions are not interchangeable
    obs: dict = pydantic.Field(default_factory=dict)
    success: bool = False
    done: bool = False
    info: dict = pydantic.Field(default_factory=dict)

    def __add__(self, other: 'SubTransition') -> 'SubTransition':
        assert not set(self.obs.keys()) & set(other.obs.keys()), f"Overlapping keys: {set(self.obs.keys()) & set(other.obs.keys())}"
        assert not set(self.info.keys()) & set(other.info.keys()), f"Overlapping keys: {set(self.info.keys()) & set(other.info.keys())}"
        return SubTransition(
            obs={**self.obs, **other.obs},
            success=self.success or other.success,
            done=self.done or other.done,
            info={**self.info, **other.info}
        )


class TransitionObservation(pydantic.BaseModel, extra="forbid"):
    # An observation is everything the agent should be aware of.
    observation: Observation
    success: bool
    done: bool
    # Info contains anything that systems around the agent need but not the agent itself
    # It's purposefully not typed to allow for flexibility.
    info: dict


class SetupInput(pydantic.BaseModel, extra="forbid"):
    start_url: str


class AgentAction(pydantic.BaseModel, extra="allow"):
    code: str = pydantic.Field(..., min_length=1)

    cost: float = 0.  # it's default 0. because we don't always have a cost, e.g. for noop actions and init
    description: str = ""
    metadata: dict = pydantic.Field(default_factory=dict)


class SetupOutput(pydantic.BaseModel, extra="forbid"):
    init_acts: tuple[AgentAction, ...] = tuple()
    exec_context: dict = pydantic.Field(default_factory=dict)


class AgentActionRequest(pydantic.BaseModel, extra="forbid"):
    observation: Observation
    mode: SupportedModes


NOOP_ACTION = AgentAction(code="pass")
