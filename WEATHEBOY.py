import requests

api_key = "e1e529b7960ad4916fe80aabff20a8bb"

city = input("Enter city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print("Temperature:", temp, "°C")
    print("Weather:", weather)

else:
    print("City not found")
