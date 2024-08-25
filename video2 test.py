import pytest
from video2 import get_git_user

def test_get_git_user(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'login': 'zavr', "id": "277472", "name":"Завр"}
    result = get_git_user('zavr')
    assert result['login'] == 'zavr' and result['id'] == '277472' and result['name'] == 'Завр'

def test_get_git_user_with_error(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404
    result = get_git_user('zavr')
    assert result is None