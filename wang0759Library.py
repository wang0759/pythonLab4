import math


# calculate the MPG
def calculateMpg(miles,gallons):
    mpg = miles/gallons
    return mpg
  
# calculate the area of a given circle
def calculateAreaOfCircle(r):
    areaCircle = math.pi*r**2
    return areaCircle
 
    
# convert Fahrenheit to celsius degree
def convertFahrenheitToCelsius(fah):
    cel = (fah - 32) * 5 / 9
    return cel


# calculate the distance between any given points
def calculateDistanceBetweenPoints(x,y, x1,y1):

    distance = math.sqrt((x - x1)**2 + (y - y1)**2)
    return distance
