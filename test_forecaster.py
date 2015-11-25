import pytest
import mock
from mock import Mock
from forecaster import Forecaster, WeatherService

@pytest.fixture
def mock_ws():
    return Mock(spce=WeatherService)

@pytest.mark.parametrize(
                "reading, expected_forecast",
                [
                    ('rising', 'Going to rain'),
                    ('falling', 'Looks clear'),
                ]
)
def test_forecast(reading, expected_forecast, mock_ws):
    forecaster = Forecaster(mock_ws)
    mock_ws.barometer.return_value = reading
    assert forecaster.forecast() == expected_forecast

