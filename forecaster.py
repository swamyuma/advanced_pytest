import random

class WeatherService(object):
    def barometer(self):
        return random.choice(['rising', 'falling'])    
        
class Forecaster(object):
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def forecast(self):
        reading = self.weather_service.barometer()
        forecasts = dict(
                        rising = 'Going to rain',
                        falling = 'Looks clear'
                        )
        return forecasts[reading]
    

