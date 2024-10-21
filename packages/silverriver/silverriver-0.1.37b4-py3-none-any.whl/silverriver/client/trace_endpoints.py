from silverriver.client.endpoint import Endpoint
from silverriver.interfaces.data_models import (WorkflowRunResponse, TraceProcessingStatus, TraceRequestModel,
                                                UserStory, LogsRequestModel)


class TraceEndpoints:
    PREFIX = "/api/v1/trace"
    UPLOAD = Endpoint(
        prefix=PREFIX, path="/upload",
        method="POST",
        request_model=TraceRequestModel,
        response_model=bool,
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


class QAEndpoints:
    PREFIX = "/api/v1/qa"
    RUN_TEST = Endpoint(prefix=PREFIX, path="/run", method="POST",
                        request_model=None,
                        response_model=bool)

    LATEST_RESULTS = Endpoint(
        prefix=PREFIX, path="/results/latest", method="GET",
        request_model=None,
        response_model=WorkflowRunResponse
    )

    PW_TRACES = Endpoint(
        prefix=PREFIX,
        path="/playwright-traces",
        method="GET",
        request_model=None,
        response_model=bytes,
    )

    # TODO (d3sm0): Not sure if this endpoint should be qa or something else
    UPLOAD_TEST_LOGS = Endpoint(
        prefix=PREFIX,
        path="/logs",
        method="POST",
        request_model=LogsRequestModel,
        response_model=bool,
    )
