from wang0759 import *

calculateMpg(miles,gallons)

calculateAreaOfCircle(r)

convertFahrenheitToCelsius(fah)

def calculateDistanceBetweenPoints(x,y, x1,y1):

    distance = math.sqrt((x - x1)**2 + (y - y1)**2)
    return distance
  
def calculateMpg(miles,gallons):
    mpg = miles/gallons
    return mpg
  
def calculateAreaOfCircle(r):
    areaCircle = math.pi*r**2
    return areaCircle
  
def convertFahrenheitToCelsius(fah):
    cel = (fah - 32) * 5 / 9
    return cel


