import pytest
import mock
from mock import Mock
from forecaster import Forecaster
from weather_service import WeatherService

@pytest.fixture
def mock_ws():
    return Mock(spec=WeatherService)

@pytest.mark.parametrize(
                "reading, expected_forecast",
                [
                    ('rising', 'Going to rain'),
                    ('falling', 'Looks clear'),
                ], ids=["rain", "clear"]
)
def test_forecast(reading, expected_forecast, monkeypatch, mock_ws):
    '''
    1. Assume that the forecaster module imports an external module weatherservice and 
    then instantiates it in the constructor.
    2. In this case you cannot inject a mock into forecaster's constructor.
    3. Therefore, use a monkeypatching. Pytest will only patch a value for the duration
    of the test and then remove it.
    '''
    WS = Mock(return_value=mock_ws) 
    monkeypatch.setattr('forecaster.WeatherService', WS)
    forecaster = Forecaster()
    mock_ws.barometer.return_value = reading
    assert 0

