import pytest

from discount import apply_discount

@pytest.mark.parametrize("price, percent, expected", [
    (100, 0, 100),
    (100, 50, 50),
    (100, 100, 0),
    (200, 25, 150),
    (50, 10, 72),
])

def discount_calculation(price, percent, expected):
    assert apply_discount(price, percent) == expected
