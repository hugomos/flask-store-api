from typing import TypeVar
from infra.http.ports.errors import ServerError
from infra.http.ports.http_status_codes import HttpStatusCode

from flask import Response, jsonify


Input = TypeVar("Input")


def bad_request(error: Exception) -> Response:
    return jsonify({
        "message": str(error),
        "success": False
    }), HttpStatusCode.BAD_REQUEST


def ok(data: Input) -> Response:
    return jsonify({
        "data": data,
        "message": "OK",
        "success": True
    }), HttpStatusCode.OK


def server_error(error: Exception) -> Response:
    return jsonify({
        "message": ServerError(str(error)).message,
        "success": False
    }), HttpStatusCode.INTERNAL_SERVER_ERROR


def no_content() -> Response:
    return jsonify({
        "message": "No Content",
        "success": True
    }), HttpStatusCode.NO_CONTENT


def unauthorized() -> Response:
    return jsonify({
        "message": "Unauthorized",
        "success": False
    }), HttpStatusCode.UNAUTHORIZED
