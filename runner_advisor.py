import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("openweather_api_key")

def get_weather(api_key):
    lat = 33.52
    lon = -5.10
    url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        temp=data['main']['temp']
        return temp
    else:
        return None
        


  




    
  
def get_advice(temp):
    if temp < 0:
        return "Heavy Winter Gear: Thermals, windbreaker, gloves, and beanie."
    elif 0 <= temp < 5:
        return "Cold Gear: Long-sleeve base layer, windbreaker, and leggings."
    elif 5 <= temp < 10:
        return "Light Layers: Long-sleeve tech shirt and leggings/capris."
    elif 10 <= temp < 15:
        return "Ideal Conditions: Short-sleeve tee and shorts."
    elif 15 <= temp < 20:
        return "Warm Weather: Tank top and shorts. Don't forget sunscreen!"
    else:
        return "Hot Weather: Lightest gear possible and carry water/electrolytes."

        


print("Welcome AUI runners, this app uses science to make you wear the most efficient clothes for your run depending on the weather.")

temperature=get_weather(api_key) 
if temperature is not None:
    advice=get_advice(temperature)
    print(f"[LIVE] The temperature now is {round(temperature,2)} C")
    print(f"What is recommended to wear is:")
    print(advice)
    
else:
      
    print("⚠️ Sorry, I can't reach the weather station right now. Wear a windbreaker just in case!")

print("Thank you for trusting us! Good luck with the training. ")
        

