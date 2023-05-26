import requests
import json
import win10toast

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=YOUR_API_KEY")


if response.status_code == 200:

    data = response.json()

    print(data)

    with open('weather.json', 'w') as f:
        json.dump(data, f)

    print(data['main']['temp'])

    print(data['weather'][0]['description'])

    print(data['wind']['speed'])

    print(data['sys']['sunrise'])

    print(data['sys']['sunset'])
    
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Weather", "The weather in London is " + data['weather'][0]['description'], duration=10)
else:
    print("Something went wrong")
