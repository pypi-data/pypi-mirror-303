
from silverriver.client.endpoint import Endpoint
from silverriver.interfaces.data_models import WorkflowRunResponse, TraceProcessingStatus, TraceRequestModel, UserStory, RunTestRequestModel, WorkflowRequestModel, TestRequestModel


class TraceEndpoints:
    PREFIX = "/api/v1/trace"
    UPLOAD = Endpoint(
        prefix=PREFIX, path="/upload",
        method="POST",
        request_model=TraceRequestModel,
        response_model=bool,
    )

    RUN_TEST = Endpoint(prefix=PREFIX, path="/run_test", method="POST",
                        request_model=RunTestRequestModel,
                        response_model=bool)

    GET_LATEST_RESULTS = Endpoint(
        prefix=PREFIX, path="/latest_results", method="GET",
        request_model=WorkflowRequestModel,
        response_model=WorkflowRunResponse
    )
    STATUS = Endpoint(
        prefix=PREFIX, path="/status", method="GET",
        request_model=str,
        response_model=TraceProcessingStatus,
    )
    GET_USER_STORY = Endpoint(
        prefix=PREFIX, path="/user_story", method="GET",
        request_model=str,
        response_model=UserStory,
    )
    EDIT_USER_STORY = Endpoint(
        prefix=PREFIX, path="/edit_user_story", method="POST",
        request_model=str,
        response_model=UserStory,
    )

    GET_TEST_LOGS = Endpoint(
        prefix=PREFIX,
        path="/logs",
        method="GET",
        request_model=TestRequestModel,
        response_model=bytes,
    )
