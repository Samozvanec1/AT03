import pytest
from DZ import get_cat

def test_get_cat(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'test'
    result = get_cat()
    assert result == b'test'

def test_get_cat_with_error(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404
    result = get_cat()
    assert result is None
