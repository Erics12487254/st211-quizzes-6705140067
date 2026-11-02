"Exercise 3"

from unittest.mock import Mock
import pytest
def test_side_effect_exception():
    mock = Mock()
    mock.login.side_effect = ValueError(
        "Invalid credentials"
    )
    with pytest.raises(ValueError):
        mock.login()

#Ex A: change ValueError to RuntimeError
#Ex B: remove with pytest.raises(...)