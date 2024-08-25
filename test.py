from main import weather
import pytest

def test_weather(mocker):
    mock_get = mocker.patch('main.requests.get') # mock requests.get - это функция из библиотеки requests
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'weather': [{'description': 'sunny'} ],'main':{'temp': 10}}
    result = weather('London', 'this api key is my too, OKAY')
    assert result['weather'][0]['description'] == 'sunny' and result['main']['temp'] == 10

def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    result = weather('Lоndоn', 'it is my api key, okay')
    assert result is None
