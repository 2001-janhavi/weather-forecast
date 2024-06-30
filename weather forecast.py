# Import the requests library to send HTTP requests using Python
import requests


# Prompt the user to enter the city name
city_name = input("Enter City Name:")

api_key = "1f1823ceac0945aec10e8ec784bcc0ba"  # Replace this with your own API key

# Construct the API request URL by concatenating the API endpoint with the city name and API key
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

# Send an HTTP GET request to the OpenWeatherMap API
response = requests.get(url)

# Check if the API response is successful
if response.status_code == 200:
    # Convert the JSON response to a Python dictionary
    data = response.json()


if response.status_code == 200:
    # Convert the JSON response to a Python dictionary
    data = response.json()

     # Extract the weather information from the JSON response
    weather_main = data['weather'][0]['main']
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Print the extracted weather information to the console 
    print(f"Weather: {weather_main}, {weather_description}")

    #print temperature in Celsius and Kelvin in same line
    print(f"Temperature: {temperature} K", end = " ")
    temperature_celsius = round(temperature - 273.15, 2)
    print(f"= {temperature_celsius} °C")

    #print humidity and wind speed 
    print(f"Humidity: {humidity} %")
    print(f"Wind Speed: {wind_speed} m/s")

# Check if the API response is a 404 error
elif response.status_code == 404:
        print("City not found.")
else:
    # Print an error message if the API request fails for any other reason
    print("Error occurred during the API request.")