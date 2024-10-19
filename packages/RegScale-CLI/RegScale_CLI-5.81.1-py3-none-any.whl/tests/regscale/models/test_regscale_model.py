import pytest
from unittest.mock import patch
from regscale.models.regscale_models.regscale_model import RegScaleModel


class TestModel(RegScaleModel):
    _unique_fields = ["name"]
    name: str
    value: int


@pytest.fixture
def mock_api_handler():
    with patch("regscale.models.regscale_models.regscale_model.APIHandler") as mock:
        yield mock


@pytest.fixture
def mocked_model():
    with patch.object(TestModel, "get_cached_object") as mock_get_cached, patch.object(
        TestModel, "find_by_unique"
    ) as mock_find, patch.object(TestModel, "cache_object") as mock_cache, patch.object(
        TestModel, "create"
    ) as mock_create, patch.object(
        TestModel, "_perform_save"
    ) as mock_perform_save:

        yield TestModel(name="test", value=1), {
            "get_cached": mock_get_cached,
            "find": mock_find,
            "cache": mock_cache,
            "create": mock_create,
            "perform_save": mock_perform_save,
        }


def test_create_new_instance(mocked_model):
    model, mocks = mocked_model
    mocks["get_cached"].return_value = None
    mocks["find"].return_value = None
    mocks["create"].return_value = TestModel(id=1, name="test", value=1)

    result = model.create_or_update()

    assert result.id == 1
    mocks["create"].assert_called_once()
    mocks["perform_save"].assert_not_called()


def test_update_existing_instance(mocked_model):
    model, mocks = mocked_model
    cached_instance = TestModel(id=2, name="test", value=2)
    mocks["get_cached"].return_value = cached_instance
    model.value = 3  # This change should trigger an update
    mocks["perform_save"].return_value = TestModel(id=2, name="test", value=3)

    result = model.create_or_update()

    assert model._original_data == {
        "id": 2,
        "name": "test",
        "value": 2,
    }, "Original data should be set to cached instance data"
    assert result.id == 2
    assert result.value == 3
    mocks["perform_save"].assert_called_once()
    assert model._original_data == {"id": 2, "name": "test", "value": 2}, "Original data should not change after save"


def test_no_update_when_no_changes(mocked_model):
    model, mocks = mocked_model
    cached_instance = TestModel(id=3, name="test", value=1)
    mocks["get_cached"].return_value = cached_instance

    result = model.create_or_update()

    mocks["get_cached"].assert_called_once()
    mocks["perform_save"].assert_not_called()

    assert result == cached_instance, "Should return the cached instance without changes"
    assert model._original_data == cached_instance.dict(
        exclude_unset=True
    ), "Original data should be set to cached instance data"

    print(f"Result: {result}")
    print(f"Cached instance: {cached_instance}")
    print(f"Model _original_data: {model._original_data}")


@pytest.mark.parametrize(
    "initial_value,new_value,expected_calls",
    [
        (1, 2, 1),  # Different value, should update
        (1, 1, 0),  # Same value, should not update
    ],
)
def test_update_behavior(mocked_model, initial_value, new_value, expected_calls):
    model, mocks = mocked_model
    cached_instance = TestModel(id=1, name="test", value=initial_value)
    mocks["get_cached"].return_value = cached_instance
    model.value = new_value
    mocks["perform_save"].return_value = TestModel(id=1, name="test", value=new_value)

    model.create_or_update()

    assert mocks["perform_save"].call_count == expected_calls


if __name__ == "__main__":
    pytest.main()
