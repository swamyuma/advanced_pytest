# Advanced pytest
## Passing commandline arguments to pytest
Pass input arguments from commandline to test file
### Command
```sh
py.test -s -q test_slide_number.py --slide_number "Slide1"

py.test -s -q test_slide_number.py --slide_number "Slide2"
```
## Test parametrization
Use `pytest.mark.parametrize` to test website title on `Firefox` and `Chrome` browsers
### Reference
https://www.youtube.com/watch?v=LdVJj65ikRY

https://blogs.gnome.org/danni/2012/11/15/combining-py-test-and-selenium-to-test-webapps/
### Command
```sh
py.test -s -q test_website_title.py
```
## Using pytest and mock libraries
Use pytest with mock library to test weather forecast module. This is a demo of 
* using mock library to inject a third party module `WeatherService` into `Forecast` module constructor
* using mark `params` with `node IDs` and run tests based on their `IDs`
* using `assert 0` to observe a failing test
* notice how each iteration of the failing test is marked with its `IDs`, e.g.
  * `test_forecast[rain]`
  * `test_forecast[clear]`

### Command
```sh
py.test -v -rf test_forecaster.py
```
This test will generate a report similar to
```sh
platform darwin -- Python 2.7.10 -- py-1.4.27 -- pytest-2.7.1 -- /Users/demouser/anaconda/bin/python
rootdir: /Users/demouser/scripts/advanced_pytest, inifile:
collected 2 items

test_forecaster.py::test_forecast[rain] FAILED
test_forecaster.py::test_forecast[clear] FAILED

==================================================== FAILURES =====================================================
_______________________________________________ test_forecast[rain] _______________________________________________

reading = 'rising', expected_forecast = 'Going to rain'
monkeypatch = <_pytest.monkeypatch.monkeypatch instance at 0x102efdf38>
mock_ws = <Mock spec='WeatherService' id='4344188688'>

    @pytest.mark.parametrize(
                    "reading, expected_forecast",
                    [
                        ('rising', 'Going to rain'),
                        ('falling', 'Looks clear'),
                    ], ids=["rain", "clear"]
    )
    def test_forecast(reading, expected_forecast, monkeypatch, mock_ws):
        WS = Mock(return_value=mock_ws)
        monkeypatch.setattr('forecaster.WeatherService', WS)
        forecaster = Forecaster()
        mock_ws.barometer.return_value = reading
>       assert 0
E       assert 0

test_forecaster.py:23: AssertionError
______________________________________________ test_forecast[clear] _______________________________________________

reading = 'falling', expected_forecast = 'Looks clear'
monkeypatch = <_pytest.monkeypatch.monkeypatch instance at 0x102f0dd40>
mock_ws = <Mock spec='WeatherService' id='4344325392'>

    @pytest.mark.parametrize(
                    "reading, expected_forecast",
                    [
                        ('rising', 'Going to rain'),
                        ('falling', 'Looks clear'),
                    ], ids=["rain", "clear"]
    )
    def test_forecast(reading, expected_forecast, monkeypatch, mock_ws):
        WS = Mock(return_value=mock_ws)
        monkeypatch.setattr('forecaster.WeatherService', WS)
        forecaster = Forecaster()
        mock_ws.barometer.return_value = reading
>       assert 0
E       assert 0

test_forecaster.py:23: AssertionError
============================================= short test summary info =============================================
FAIL test_forecaster.py::test_forecast[rain]
FAIL test_forecaster.py::test_forecast[clear]
============================================ 2 failed in 0.01 seconds =============================================
```
### Reference
* https://www.youtube.com/watch?v=RcN26hznmk4
* https://www.youtube.com/watch?v=AiThU6JQbE8
