# Name: Group 2 (Alexander Fletcher and Sean Dippold)
# email: fletchax@mail.uc.edu and dippolst@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: Noc 9, 2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: PyDev project to pull from an API into python, and then pull a segment of data from that data.
# Citations: NA
# Anything else that's relevant: NA

import json
import requests

#pulls the data from the url and makes it into a python dictionary
response = requests.get('https://api.weather.gov/gridpoints/ILN/36,38/forecast')
json_string = response.content
parsed_json = json.loads(json_string)

#creates a class called Weather, and pulls the next time of day, its temperature, and its temperature unit as a string
class Weather:
    def __str__(self):
        for weather in parsed_json['properties']['periods']:
            return str(weather['name'])+", Temperature: "+str(weather['temperature'])+str(weather['temperatureUnit'])
