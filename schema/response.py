from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List


# ==================== BASE RESPONSE ====================


class BaseResponse(BaseModel):
    """Base response model for all API responses."""

    success: bool = Field(default=True, description="Whether the request was successful")
    message: str = Field(default="", description="Response message")
    data: Optional[dict] = Field(default=None, description="Response data (use typed models in subclasses)")


# ==================== SWAGGER ERROR RESPONSE MODELS ====================


class ErrorDetail(BaseModel):
    field: str = Field(..., description="Dot-separated path to the invalid field", examples=["body.email"])
    message: str = Field(..., description="Human-readable validation error message", examples=["value is not valid"])
    type: str = Field(..., description="Machine-readable error type identifier", examples=["value_error"])


class ErrorBody(BaseModel):
    status_code: int = Field(..., description="HTTP status code", examples=[400])
    status_message: str = Field(..., description="HTTP status text", examples=["BAD REQUEST"])
    message: str = Field(..., description="User-friendly error message", examples=["Invalid request."])
    code: Optional[str] = Field(None, description="Machine-readable error code", examples=["BAD_REQUEST"])
    details: Optional[List[ErrorDetail]] = Field(None, description="Field validation errors (only for 422)")


class BadRequestResponse(BaseModel):
    success: bool = Field(default=False, description="Always false for error responses")
    error: ErrorBody

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "error": {
                    "status_code": 400,
                    "status_message": "BAD REQUEST",
                    "message": "Invalid request. Please check your input.",
                    "code": "BAD_REQUEST",
                },
            }
        }
    )


class UnauthorizedResponse(BaseModel):
    success: bool = Field(default=False, description="Always false for error responses")
    error: ErrorBody

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "error": {
                    "status_code": 401,
                    "status_message": "UNAUTHORIZED",
                    "message": "Please log in to continue.",
                    "code": "UNAUTHORIZED",
                },
            }
        }
    )


class ForbiddenResponse(BaseModel):
    success: bool = Field(default=False, description="Always false for error responses")
    error: ErrorBody

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "error": {
                    "status_code": 403,
                    "status_message": "FORBIDDEN",
                    "message": "You don't have permission to access this resource.",
                    "code": "FORBIDDEN",
                },
            }
        }
    )


class NotFoundResponse(BaseModel):
    success: bool = Field(default=False, description="Always false for error responses")
    error: ErrorBody

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "error": {
                    "status_code": 404,
                    "status_message": "NOT FOUND",
                    "message": "The requested resource was not found.",
                    "code": "NOT_FOUND",
                },
            }
        }
    )


class ConflictResponse(BaseModel):
    success: bool = Field(default=False, description="Always false for error responses")
    error: ErrorBody

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "error": {
                    "status_code": 409,
                    "status_message": "CONFLICT",
                    "message": "This resource already exists.",
                    "code": "CONFLICT",
                },
            }
        }
    )


class ValidationErrorResponse(BaseModel):
    success: bool = Field(default=False, description="Always false for error responses")
    error: ErrorBody

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "error": {
                    "status_code": 422,
                    "status_message": "UNPROCESSABLE ENTITY",
                    "message": "Please check your input and try again.",
                    "code": "VALIDATION_ERROR",
                    "details": [
                        {
                            "field": "body.email",
                            "message": "value is not a valid email address",
                            "type": "value_error.email",
                        }
                    ],
                },
            }
        }
    )


class RateLimitResponse(BaseModel):
    success: bool = Field(default=False, description="Always false for error responses")
    error: ErrorBody

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "error": {
                    "status_code": 429,
                    "status_message": "TOO MANY REQUESTS",
                    "message": "Rate limit exceeded. Please try again later.",
                    "code": "RATE_LIMITED",
                },
            }
        }
    )


class InternalServerErrorResponse(BaseModel):
    success: bool = Field(default=False, description="Always false for error responses")
    error: ErrorBody

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "error": {
                    "status_code": 500,
                    "status_message": "INTERNAL SERVER ERROR",
                    "message": "Something went wrong. Please try again later.",
                    "code": "INTERNAL_ERROR",
                },
            }
        }
    )


class BadGatewayResponse(BaseModel):
    success: bool = Field(default=False, description="Always false for error responses")
    error: ErrorBody

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "error": {
                    "status_code": 502,
                    "status_message": "BAD GATEWAY",
                    "message": "Service temporarily unavailable. Please try again later.",
                    "code": "EXTERNAL_SERVICE_ERROR",
                },
            }
        }
    )


class ServiceUnavailableResponse(BaseModel):
    success: bool = Field(default=False, description="Always false for error responses")
    error: ErrorBody

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": False,
                "error": {
                    "status_code": 503,
                    "status_message": "SERVICE UNAVAILABLE",
                    "message": "Service temporarily unavailable. Please try again later.",
                    "code": "SERVICE_UNAVAILABLE",
                },
            }
        }
    )


# ==================== COMMON SWAGGER RESPONSES ====================

COMMON_ERROR_RESPONSES = {
    401: {
        "model": UnauthorizedResponse,
        "description": "Authentication required or token invalid/expired",
    },
    422: {
        "model": ValidationErrorResponse,
        "description": "Request body failed schema validation",
    },
    429: {
        "model": RateLimitResponse,
        "description": "Rate limit exceeded for this endpoint",
    },
    500: {
        "model": InternalServerErrorResponse,
        "description": "Unexpected server error",
    },
}
