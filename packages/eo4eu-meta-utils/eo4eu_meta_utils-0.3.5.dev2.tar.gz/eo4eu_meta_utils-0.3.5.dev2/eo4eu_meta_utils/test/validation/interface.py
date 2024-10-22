from abc import ABC, abstractmethod
from typing import Any, Self


class ValidationError(Exception):
    pass


class Matcher(ABC):
    # this is supposed to raise a ValidationError if the value is invalid
    @abstractmethod
    def match(self, value: Any):
        raise ValidationError("")


class Field:
    def __init__(self, is_required: bool, payload: Any):
        self._is_required = is_required
        self._payload = payload

    def is_required(self) -> bool:
        return self._is_required

    def payload(self) -> Any:
        return self._payload

    @classmethod
    def req(cls, payload: Any) -> Self:
        return Field(True, payload)

    @classmethod
    def opt(cls, payload: Any) -> Self:
        return Field(False, payload)
