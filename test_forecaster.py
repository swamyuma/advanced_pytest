import pytest
import mock
from mock import Mock
from forecaster import Forecaster, WeatherService

@pytest.fixture
def mock_ws():
    return Mock(spce=WeatherService)

def test_rain_when_barometer_rising(mock_ws):
    forecaster = Forecaster(mock_ws)
    mock_ws.barometer.return_value = 'rising'
    assert forecaster.forecast() == 'Going to rain'

def test_clear_when_barometer_falling(mock_ws):
    forecaster = Forecaster(mock_ws)
    mock_ws.barometer.return_value = 'falling'
    assert forecaster.forecast() == 'Looks clear'
