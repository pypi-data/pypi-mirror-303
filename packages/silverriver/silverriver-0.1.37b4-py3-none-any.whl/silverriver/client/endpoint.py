from typing import Literal

import pydantic


class Endpoint(pydantic.BaseModel):
    prefix: str
    path: str
    method: Literal["GET", "POST"]
    response_model: type[pydantic.BaseModel] | type | None
    request_model: type[pydantic.BaseModel] | type | None

    def request_args(self, data: pydantic.BaseModel | None = None, files: pydantic.BaseModel | None = None) -> dict:
        # The goal of this code is to capture malformed request prior that they leave the client.
        params = dict(endpoint=self.prefix + self.path, method=self.method, response_model=self.response_model)
        if data is not None:
            assert isinstance(data, self.request_model), f"Expected {self.request_model}, got {type(data)}"
            params["data"] = data.model_dump()
        if files is not None:
            assert isinstance(files, self.request_model), f"Expected {self.request_model}, got {type(files)}"
            params["files"] = files.model_dump()
        return params
