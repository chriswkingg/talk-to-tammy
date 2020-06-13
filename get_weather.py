import pyowm
owm = pyowm.OWM('9127ba2b10dc154a02ee18c53896f988')
def getTemp(loc):
    try:
        location = loc
        w = owm.weather_at_place(location)
        weather = w.get_weather()
        return "Tempurature in " + location + " is " + str(weather.get_temperature('celsius')['temp']) + " degrees celsius."
    except pyowm.exceptions.api_response_error.NotFoundError:
        return "Unable to find location, please try again or reword"
        
