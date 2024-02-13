from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
import requests
from datetime import datetime

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')

class WeatherApp(App):
    def build(self):
        # Layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Title Label
        title_label = Label(text="Weather Information", font_size=24)
        layout.add_widget(title_label)

        # Get Weather Data
        api_key = '24faddfc133a855786488692d3d0ade2'  # Replace with your actual OpenWeatherMap API key
        city_id = '1734810'  # Replace with your desired city ID This is seremban
        weather_data = self.get_weather(api_key, city_id)

        if weather_data:
            # Display Weather Information
            self.display_weather(layout, weather_data)
        else:
            # Display Error Message
            error_label = Label(text="Failed to fetch weather data.", font_size=20)
            layout.add_widget(error_label)

        return layout

    def get_weather(self, api_key, city_id):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'id': city_id,
            'appid': api_key,
            'units': 'metric',  # Use 'imperial' for Fahrenheit
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return None

    def display_weather(self, layout, weather_data):
        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_description = weather_data['weather'][0]['description']

        sunrise_timestamp = weather_data['sys']['sunrise']
        sunset_timestamp = weather_data['sys']['sunset']

        # Convert timestamps to readable time format
        sunrise_time = datetime.utcfromtimestamp(sunrise_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        sunset_time = datetime.utcfromtimestamp(sunset_timestamp).strftime('%Y-%m-%d %H:%M:%S')

        # Display Weather Information
        layout.add_widget(Label(text=f"City: {city_name}", font_size=20))
        layout.add_widget(Label(text=f"Temperature: {temperature}°C", font_size=20))
        layout.add_widget(Label(text=f"Humidity: {humidity}%", font_size=20))
        layout.add_widget(Label(text=f"Wind Speed: {wind_speed} m/s", font_size=20))
        layout.add_widget(Label(text=f"Weather Description: {weather_description}", font_size=20))
        layout.add_widget(Label(text=f"Sunrise Time: {sunrise_time}", font_size=20))
        layout.add_widget(Label(text=f"Sunset Time: {sunset_time}", font_size=20))

if __name__ == "__main__":
    WeatherApp().run()
