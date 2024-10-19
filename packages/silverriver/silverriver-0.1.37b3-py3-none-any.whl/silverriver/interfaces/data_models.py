import enum
from datetime import datetime
from typing import Optional, Any

import pydantic
from pydantic import BaseModel, Field, field_validator

MAX_FILE_SIZE = 1024 ** 2 * 50  # 50mb

SYSTEM_ROLE = "system"
HUMAN_ROLE = "user"
ASSISTANT_ROLE = "assistant"


class ChatMessage(pydantic.BaseModel):
    role: str  # TODO: make this an enum
    message: str
    timestamp: float
    message_id: int | str | None = None


class BrowserObservation(pydantic.BaseModel, extra="forbid"):
    axtree_txt: str
    screenshot_som: str  # base64 encoded image
    url: str
    network_requests: str
    last_browser_error: str


class Observation(BrowserObservation, extra="forbid"):
    chat_messages: list[ChatMessage]
    # TODO: To make this class public we should rename some fields to be more general
    last_action_error: str

class WorkflowStatus(enum.StrEnum):
    REQUESTED = "requested"
    WAITING = "waiting"
    PENDING = "pending"
    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class WorkflowConclusion(enum.StrEnum):
    SUCCESS = "success"
    FAILURE = "failure"
    NEUTRAL = "neutral"
    CANCELLED = "cancelled"
    TIMED_OUT = "timed_out"
    ACTION_REQUIRED = "action_required"
    STARTUP_FAILURE = "startup_failure"
    SKIPPED = "skipped"
    STALE = "stale"



class TestResult(BaseModel):
    name: str
    status: Optional[WorkflowStatus] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    conclusion: Optional[WorkflowConclusion] = None

class WorkflowRunResponse(BaseModel):
    name: str
    status: Optional[WorkflowStatus] = None
    conclusion: Optional[WorkflowConclusion] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    test_results: list[TestResult] = Field(default_factory=list)


class WorkflowRequestModel(BaseModel, extra="forbid"):
    workflow_id: str


class TraceProcessingStatus(enum.StrEnum):
    NO_TRACE = "NO_TRACE"
    NO_USER_STORY = "NO_USER_STORY"
    TO_BE_CONFIRMED = "TO_BE_CONFIRMED"
    ERROR = "ERROR"


class TraceProcessingState(BaseModel):
    state: TraceProcessingStatus


class UserStory(pydantic.BaseModel):
    story_name: str
    story: str


class TraceRequestModel(pydantic.BaseModel):
    filename: str
    content: bytes

    @field_validator("content")
    @classmethod
    def check_content_size(cls, content: bytes) -> Any:
        if len(content) == 0:
            raise ValueError("Content is empty")
        if len(content) > MAX_FILE_SIZE:
            max_size_mb = MAX_FILE_SIZE // (1024 ** 2)
            raise ValueError(f"Content is too large, must be less than {max_size_mb} MB")
        return content

    def model_dump(self, **kwargs) -> dict[str, Any]:
        return {"trace": (self.filename, self.content)}


class TestRequestModel(BaseModel, extra="forbid"):
    test_id: str


class RunTestRequestModel(BaseModel, extra="forbid"):
    workflow_id: str
    test_id: str
