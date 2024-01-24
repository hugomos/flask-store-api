from typing import Optional, TypeVar

from domain.use_case import UseCase

from infra.http.ports.http_mapper import HttpMapper
from infra.http.ports.http_response import no_content, bad_request, ok, server_error

from flask import Response, request


Input = TypeVar("Input")
Output = Response


class HttpController:
    def __init__(self, use_case: UseCase, mapper: HttpMapper):
        self.__use_case = use_case
        self.__mapper = mapper

    def handle(self, id: Optional[str] = None) -> Output:
        try:
            body = request.json if request.is_json else {}
            data = {**body}

            if id:
                data["id"] = id

            use_case_output = self.__use_case.perform(data)

            if use_case_output.is_left():
                return bad_request(use_case_output.value)

            if type(use_case_output.value) is list and len(use_case_output.value) == 0:
                return no_content()

            if not use_case_output.value:
                return no_content()

            if self.__mapper:
                return ok(self.__mapper.map(use_case_output.value))

            return ok(use_case_output.value)
        except Exception as e:
            return server_error(e)
