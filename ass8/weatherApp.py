import requests
def get_weather(city, api_key):
    url=f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    
    response=requests.get(url)
    data=response.json()
    
    if "current" in data:
        temp_c=data["current"]["temp_c"]
        condition=data["current"]["condition"]["text"]
        humidity=data["current"]["humidity"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temp_c}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        
    else:
        print("\n city not found.")

if __name__=="__main__":
    city=input("Enter city name:")
    api_key="04a73f4437ab4160ae4100640250902"
    get_weather(city, api_key)