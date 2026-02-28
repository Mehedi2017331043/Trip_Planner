import requests

class WeatherForecast:
    def __init__(self, api_key: str):
        self.api_key = api_key 
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self, place: str):
        """ Get current weather of a place """
        try:
            url = f'{self.base_url}/weater'
            params = {
                "q": place,
                "appid": self.api_key
            } 
            response = requests.get(url, params=params)
            return response.json() if response.status_code==200 else {}
        except Exception as e:
            raise e
    
    def get_forecast_weather(self, place: str):
        """ Get weather forecast of place """
        try:
            url = f'{self.base_url}/forecast'
            params = {
                'q': place,
                'appid': self.api_key,
                'cnt': 10,
                'units': "mertic" 
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code==200 else {}
        
        except Exception as e:
            raise e
        

if __name__=='__main__':
    OPENWEATHERMAP_API_KEY = "380db622c2da8715c30d2858c9d888d3"
    weather_forecast = WeatherForecast(api_key=OPENWEATHERMAP_API_KEY)
    current_weather = weather_forecast.get_current_weather('Sylhet')
    print(current_weather)