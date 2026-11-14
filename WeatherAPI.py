import matplotlib.pyplot as plt
import requests
import os
from dotenv import load_dotenv
load_dotenv()

class WeatherAPI:
    def __init__(self,countryofsearch,secret_key):
        self.key = secret_key
        self.country = countryofsearch
        self.parameters = {"key" : self.key ,"q": self.country}

    def CallAPI(self):
         self.request = requests.get('https://api.weatherapi.com/v1/current.json',params=self.parameters)
         print(f"status code: {self.request.status_code}")
         if self.request.status_code != 200:
          raise Exception(f"API request failed with status code {self.request.status_code}")
         return self.request.json()

class FormattedOutput:
    def __init__(self, Data):
        self.Data = Data
    def fetch_Useful_Data(self):
        usefulData = {}
        usefulData["city_name"] = self.Data["location"]["name"]
        usefulData["country"] = self.Data["location"]["country"]
        usefulData["temp"] = self.Data["current"]["temp_c"]
        usefulData["feels_like"] = self.Data["current"]["feelslike_c"]
        usefulData["Humidity"] = self.Data["current"]["humidity"]
        usefulData["wind"] = self.Data["current"]["wind_kph"]
        usefulData["pressure"] = self.Data["current"]["pressure_mb"]
        usefulData["uv"] = self.Data["current"]["uv"]
        usefulData["conditions"] = self.Data["current"]["condition"]["text"]

        return usefulData
    def Draw_CurrentWeather_Data(self):
        UsefulData = self.fetch_Useful_Data()
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.suptitle(f"Weather Dashboard - {UsefulData['city_name']}, {UsefulData['country']}",fontsize=18,fontweight="bold")
        ax.text(0.5, 0.85, UsefulData["conditions"],  fontsize=20,ha="center",fontweight="bold")
        ax.text(0.5, 0.65, f"{UsefulData['temp']} °C", fontsize=35, ha="center", color="darkorange")
        ax.text(0.5, 0.56,f"Feels like {UsefulData['feels_like']} °C", fontsize=13,ha="center")
        Rest_info = {"Humidity" : f"{UsefulData['Humidity']} %",
                     "Wind" : f"{UsefulData['wind']} km/h",
                     "Pressure": f"{UsefulData['pressure']} mb",
                     "UV" : str(UsefulData['uv'])
                    }
        positions_on_plot = [(0.25,0.35),(0.75,0.35),(0.25,0.15),(0.75,0.15)]
        for (label,value), (px,py) in zip(Rest_info.items(), positions_on_plot):
          ax.text(px,py,label,fontsize=13,ha="center",fontweight="bold")
          ax.text(px,py - 0.05,value,fontsize=16,ha="center",color ="steelblue")
        ax.axis("off")
        plt.tight_layout()
        plt.show()

country = input("Enter the country to see the weather status: ")
if os.getenv("SECRET_KEY") is None:
    raise Exception("SECRET_KEY is not set in the environment variables. Please set it in the .env file.")
else:
 Test = WeatherAPI(countryofsearch=country,secret_key=  os.getenv("SECRET_KEY"))
 output = Test.CallAPI()
#print(output)
 format = FormattedOutput(output)
 format.Draw_CurrentWeather_Data()


