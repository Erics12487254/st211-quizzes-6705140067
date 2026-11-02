"Exercise 2"

from unittest.mock import Mock
def test_return_value():
    mock = Mock()
    mock.get_status.return_value = "OK"
    print(mock.get_status())
    print(mock.get_status())
    print(mock.get_status())
    assert mock.get_status() == "OK"

#Ex A: change OK to FAILED
#Ex B: add 3 print(mock.get_status())
#Ex C: change "OK" to 123