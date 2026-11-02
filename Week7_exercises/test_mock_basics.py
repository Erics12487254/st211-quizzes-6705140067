"Exercise 1"

from unittest.mock import Mock
def test_mock_basics():
    mock = Mock()
    result = mock.some_method() 
    print(result)
    assert isinstance(result, Mock)

#Ex A: change some_method to anything()
#Ex B: change some_method to whatever(1, 2, 3)
 
