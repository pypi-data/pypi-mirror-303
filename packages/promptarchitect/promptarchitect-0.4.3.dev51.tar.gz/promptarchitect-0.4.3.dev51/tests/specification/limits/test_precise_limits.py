import pytest
from pydantic import ValidationError
from promptarchitect.specification import PreciseLimits


def test_min_and_max_none():
    with pytest.raises(ValidationError) as excinfo:
        PreciseLimits()
    assert "You must specify at least one of min or max values." in str(excinfo.value)


def test_only_min_specified():
    limit = PreciseLimits(min=5.2)
    assert limit.min == 5.2
    assert limit.max is None


def test_only_max_specified():
    limit = PreciseLimits(max=10.1)
    assert limit.min is None
    assert limit.max == 10.1


def test_min_and_max_specified_correctly():
    limit = PreciseLimits(min=5.2, max=10.1)
    assert limit.min == 5.2
    assert limit.max == 10.1


def test_min_greater_than_max():
    with pytest.raises(ValidationError) as excinfo:
        PreciseLimits(min=10.1, max=5.2)
    assert "The min value must be less than the max value." in str(excinfo.value)
