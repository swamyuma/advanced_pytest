from weather_service import WeatherService

class Forecaster(object):
    def __init__(self):
        self.weather_service = WeatherService()

    def forecast(self):
        reading = self.weather_service.barometer()
        forecasts = dict(
                        rising = 'Going to rain',
                        falling = 'Looks clear'
                        )
        return forecasts[reading]
    

