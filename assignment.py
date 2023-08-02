import requests

def get_weather_data(location):
    api_key = "b6907d289e10d714a6e88b30761fae22"
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error retrieving weather data.")
        return None

def get_temperature(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].split()[0] == date:
            return forecast['main']['temp']
    return None

def get_wind_speed(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].split()[0] == date:
            return forecast['wind']['speed']
    return None

def get_pressure(weather_data, date):
    for forecast in weather_data['list']:
        if forecast['dt_txt'].split()[0] == date:
            return forecast['main']['pressure']
    return None

def main():
    location = "London,us"
    weather_data = get_weather_data(location)
    if not weather_data:
        return

    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting the program.")
            break
        elif choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_temperature(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature}°f")
            else:
                print("Weather data not available for the given date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Weather data not available for the given date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Weather data not available for the given date.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
