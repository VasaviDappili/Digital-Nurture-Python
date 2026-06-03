import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true"

try:

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        print("Temperature:",
              data["current_weather"]["temperature"])

        print("Wind Speed:",
              data["current_weather"]["windspeed"])

    elif response.status_code == 404:
        print("Data not found")

    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException:
    print("Network Error")