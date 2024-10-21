from typing import Self, Iterable, Any, Callable

from .interface import Matcher, Field
from .matchers import (
    EverythingMatcher,
    EqMatcher,
    NeqMatcher,
    RegexMatcher,
    AndMatcher,
    ContainsMatcher,
    LenMatcher,
    OrderedSeqMatcher,
    UnorderedSeqMatcher,
    CheckMatcher,
    ConvertMatcher,
    FieldMatcher,
    ObjectMatcher,
)


class Match(Matcher):
    def __init__(self, matcher: Matcher):
        self._matcher = matcher

    def match(self, value: Any):
        self._matcher.match(value)

    @classmethod
    def infer(cls, value: Any) -> Self:
        if isinstance(value, dict):
            return Match.obj(value)
        if isinstance(value, str):
            return Match.eq(value)
        if isinstance(value, Iterable):
            return Match.seq(value)
        return Match.eq(value)

    @classmethod
    def infer_field(cls, value: Any) -> Self:
        is_required, payload = True, value
        if isinstance(value, Field):
            is_required, payload = value.is_required(), value.payload()

        return Match(FieldMatcher(
            is_required = is_required,
            matcher = Match.infer(payload)
        ))

    @classmethod
    def any(cls) -> Self:
        return Match(EverythingMatcher())

    @classmethod
    def obj(cls, obj: dict[str,Any]) -> Self:
        return Match(ObjectMatcher(
            obj = obj,
            infer_func = cls.infer_field
        ))

    @classmethod
    def seq(
        cls,
        seq: Iterable[Any],
        input_longer: bool = True,
        input_shorter: bool = True,
    ) -> Self:
        return Match(UnorderedSeqMatcher(
            matchers = [Match.infer(value) for value in seq],
            input_longer = input_longer,
            input_shorter = input_shorter,
        ))

    @classmethod
    def eq(cls, value: Any) -> Self:
        return Match(EqMatcher(value))

    @classmethod
    def neq(cls, value: Any) -> Self:
        return Match(NeqMatcher(value))

    @classmethod
    def re(cls, pattern: str) -> Self:
        return Match(RegexMatcher(pattern))

    @classmethod
    def check(cls, func: Callable[[Any],bool], name: str = "") -> Self:
        return Match(CheckMatcher(
            func = func,
            name = name
        ))

    @classmethod
    def convert(cls, func: Callable[[Any],Any], name: str = "") -> Self:
        return Match(ConvertMatcher(
            func = func,
            name = name
        ))
