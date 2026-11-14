This repository Talks about the usage of WeatherAPI to check the current WatherStatus for a specific country.
In order to run the Python file and get the WeatherStatus you need to get a Private_Key.
To generate one you can follow this link: https://www.weatherapi.com/signup and signup or login if you already got an email on the website.
After that add the generated Private_Key to the secret_key variable in WeatherAPI.py to send a request to the WeatherAPI and get a response back.

The parameters given to the Request command are:
 1) Country => specify the country that the API will check the WeatherStatus at.
 2) key => The Private_key generated to access the API.

The response of the API is a JSON response, we got only the most important features to describe the Weather Status which are:
 1)City
 2)Country
 3)Temperature in Celsius
 4)Temperature feels like in Celsius
 5)Humidity
 6)Pressure
 7)UV
 8)Weather Condition ('overcast', 'clear', etch..)

 These 8 features are formatted to a plot to visualize and understand these 8 features:


  <img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/d6299a15-2d4d-416d-b79d-fed88d6294e1" />

 
