import pytest
from promptarchitect.specification import Limits, PropertyTestSpecification
from pydantic import ValidationError


@pytest.fixture
def valid_limits():
    return Limits(min=1, max=10)


@pytest.fixture
def invalid_limits():
    return Limits(min=10, max=1)


@pytest.fixture
def valid_property_test_spec(valid_limits):
    return PropertyTestSpecification(type="property", unit="words", limit=valid_limits)


@pytest.fixture
def invalid_property_test_spec(invalid_limits):
    return PropertyTestSpecification(
        type="property",
        unit="words",
        limit=invalid_limits,
    )


def test_property_test_spec_initialization(valid_property_test_spec):
    assert valid_property_test_spec.type == "property"
    assert valid_property_test_spec.unit == "words"
    assert valid_property_test_spec.limit.min == 1
    assert valid_property_test_spec.limit.max == 10


def test_property_test_spec_invalid_limits():
    with pytest.raises(ValidationError):
        PropertyTestSpecification(
            type="property",
            unit="words",
            limit=Limits(min=10, max=1),
        )


def test_property_test_spec_missing_limits():
    with pytest.raises(ValidationError):
        PropertyTestSpecification(type="property", unit="words", limit=Limits())


def test_property_test_spec_with_limit():
    spec = PropertyTestSpecification(type="property", unit="words", limit=Limits(min=1))

    assert spec.equals is None
    assert spec.limit is not None


def test_property_test_spec_with_equals():
    spec = PropertyTestSpecification(type="property", unit="words", equals=1)

    assert spec.limit is None
    assert spec.equals is not None


def test_limit_or_equals_must_be_set():
    with pytest.raises(ValidationError):
        PropertyTestSpecification(
            type="property",
            unit="words",
            limit=None,
            equals=None,
        )
