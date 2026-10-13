import pytest

@pytest.mark.parametrize(
    "user",
    [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
    ],
    ids=["alice-adult", "bob-adult"]
)
def test_user_has_name(user):
    assert "name" in user