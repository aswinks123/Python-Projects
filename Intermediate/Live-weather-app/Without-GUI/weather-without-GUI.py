import requests  #This module is used to sent HTTP requests


api_key='your_api_key'

user_input=input("Enter City Name:")

weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
print(weather_data.json()['cod'])
x=int(weather_data.json()['cod'])


weather_condition=weather_data.json()['weather'][0]['main']
temp=round(weather_data.json()['main']['temp'])
print(f"Current wether in  is:")
print("Weather is: ",weather_condition )
print("Temperature is: ",temp,"C")







