#build a weather app with python|weather API
import requests

api_key='26e25cf37de9a38205c8bdb5461ffec9'

user_input=input("enter city:")#getting user input

#api request
weather_data=requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")#we get this code in the documentation of the api in the perticular website
#put the status
#print(weather_data.status_code)
#print(weather_data.json())
if weather_data.json()['cod']=='404':#cod is the code for status in api
    print("no city found")
else:
   weather = weather_data.json()['weather'][0]['main']
   temp=round(weather_data.json()['main']['temp'])

   print(f"the weather in {user_input} is :{weather}")
print(f"the temperature in {user_input} is :{temp}°F")

