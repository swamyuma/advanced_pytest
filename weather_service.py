import random

class WeatherService(object):
    def barometer(self):
        return random.choice(['rising', 'falling'])    
