import re
from typing import Any, Self, Callable, Iterable

from .interface import Matcher, ValidationError


class EverythingMatcher(Matcher):
    def __init__(self):
        pass

    def match(self, value: Any):
        pass


class EqMatcher(Matcher):
    def __init__(self, value: Any):
        self._value = value

    def match(self, value: Any):
        if value != self._value:
            raise ValidationError(f"\"{value}\" is not equal to \"{self._value}\"")


class NeqMatcher(Matcher):
    def __init__(self, value: Any):
        self._value = value

    def match(self, value: Any):
        if value == self._value:
            raise ValidationError(f"\"{value}\" is equal to \"{self._value}\"")


class RegexMatcher(Matcher):
    def __init__(self, pattern: str):
        self._pattern_str = pattern
        self._pattern = re.compile(pattern)

    def match(self, value: Any):
        if not isinstance(value, str):
            raise ValidationError(f"\"{value}\" is not a string")

        if self._pattern.fullmatch(value) is None:
            raise ValidationError(f"\"{value}\" did not match regex \"{self._pattern_str}\"")


class AndMatcher(Matcher):
    def __init__(self, matchers: list[Matcher]):
        self._matchers = matchers

    def match(self, value: Any):
        for matcher in self._matchers:
            matcher.match(value)


class ContainsMatcher(Matcher):
    def __init__(self, matcher: Matcher):
        self._matcher = matcher

    def match(self, value: Any):
        if isinstance(value, Iterable):
            last_exc = None
            for val in value:
                try:
                    self._matcher.match(val)
                    return
                except ValidationError as e:
                    last_exc = e
            raise ValidationError(
                f"Failed to match any of the entries in \"{value}\". Last error: {last_exc}"
            ) from last_exc
        else:
            self._matcher.match(value)


class LenMatcher(Matcher):
    def __init__(self, min_len: int|None, max_len: int|None):
        self._min_len = min_len
        self._max_len = max_len

    def match(self, value: Any):
        if not isinstance(value, Iterable):
            raise ValidationError(f"\"{value}\" is not an iterable")

        val_len = len(value)
        if self._min_len is not None and val_len < self._min_len:
            raise ValidationError(
                f"\"{value}\" length ({val_len}) is lower than min value {self._min_len}"
            )
        if self._max_len is not None and val_len > self._max_len:
            raise ValidationError(
                f"\"{value}\" length ({val_len}) is greater than max value {self._max_len}"
            )


class OrderedSeqMatcher(Matcher):
    def __init__(self, matchers: list[Matcher], input_longer: bool = True, input_shorter: bool = True):
        self._matchers = matchers
        match_len = len(self._matchers)
        self._len_matcher = LenMatcher(
            min_len = match_len if input_longer else None,
            max_len = match_len if input_shorter else None
        )

    def match(self, value: Any):
        self._len_matcher.match(value)

        for val, matcher in zip(value, self._matchers):
            matcher.match(val)


class UnorderedSeqMatcher(Matcher):
    def __init__(self, matchers: list[Matcher], input_longer: bool = True, input_shorter: bool = True):
        self._matcher = AndMatcher([
            ContainsMatcher(matcher) for matcher in matchers
        ])
        match_len = len(matchers)
        self._len_matcher = LenMatcher(
            min_len = match_len if input_longer else None,
            max_len = match_len if input_shorter else None
        )

    def match(self, value: Any):
        self._len_matcher.match(value)
        self._matcher.match(val)


class CheckMatcher(Matcher):
    def __init__(self, func: Callable[[Any],bool], name: str = ""):
        self._func = func
        self._name = name

    def match(self, value: Any):
        try:
            if not self._func(value):
                raise ValidationError(f"\"{value}\" failed check \"{self._name}\"")
        except Exception as e:
            raise ValidationError(
                f"Failed to check \"{value}\" using \"{self._name}\": {str(e)}"
            ) from e


class ConvertMatcher(Matcher):
    def __init__(self, func: Callable[[Any],Any], name: str = ""):
        self._func = func
        self._name = name

    def match(self, value: Any):
        try:
            self._func(value)
        except Exception as e:
            raise ValidationError(
                f"Failed to convert \"{value}\" to \"{self._name}\": {str(e)}"
            ) from e


class FieldMatcher(Matcher):
    def __init__(self, is_required: bool, matcher: Matcher):
        self._is_required = is_required
        self._matcher = matcher

    def match(self, value: Any):
        was_found, inner_value = False, None
        try:
            was_found, inner_value = value
        except Exception as e:
            raise ValidationError(f"\"{value}\" could not be unpacked to 2 values")

        if was_found:
            self._matcher.match(inner_value)
        elif self._is_required:
            raise ValidationError(f"Field is required")


class ObjectMatcher(Matcher):
    def __init__(
        self,
        obj: dict[str,Any],
        infer_func: Callable[[Any],FieldMatcher]
    ):
        self._obj = {}
        for key, val in obj.items():
            if isinstance(val, dict):
                self._obj[key] = ObjectMatcher(val, infer_func)
            else:
                self._obj[key] = infer_func(val)

        self._dict_matcher = CheckMatcher(
            func = lambda val: "__getitem__" in dir(val),
            name = "is dict-like"
        )

    def match(self, value: Any):
        self._dict_matcher.match(value)
        for key, matcher in self._obj.items():
            try:
                matcher.match((True, value[key]))
            except KeyError:
                matcher.match((False, None))
