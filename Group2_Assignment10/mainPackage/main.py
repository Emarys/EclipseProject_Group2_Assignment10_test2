# Name: Group 2 (Alexander Fletcher and Sean Dippold)
# email: fletchax@mail.uc.edu and dippolst@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: Noc 9, 2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: PyDev project to pull from an API into python, and then pull a segment of data from that data.
# Citations: NA
# Anything else that's relevant: NA
import numpy as np
#imports everything from the WeatherClass module in the WeatherPackage package
from WeatherPackage.WeatherClass import *

#makes sure to only run the below if this is the main page (entry point)
if __name__ == "__main__":
    #instantiates an object of the Weather class
    currentTemp = Weather()
    #prints the data returned in the Weather class's method
    print(currentTemp)