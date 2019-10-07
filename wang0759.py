''' lab 4 Task1
Transform each of the program from last week into a stand alone function.
One function caculateMpg
One function calculateAreaOfCircle
One function convertFahrenheitToCelsius
For each function you must identify the input(s), the output(s) and provide the function body.
Each function must be properly tested using a main program that calls it.
Create a file <yourName>Library.py where <yourName> is your Algonquin user id and
transfer the 3 functions into the file.

By: Quanyi wang

'''
import library
miles = float(input("please enter miles driven:"))
gallons = float(input("please enter gallons used:"))
print("Your MPG is:", calculateMpg(miles,gallons))

# function calculateAreaOfCircle
import math
r=float(input("please enter the radius:"))
print('The area of a circle is: ', calculateAreaOfCircle(r))


# function convertFahrenheitToCelsius
fah = float(input("please enter fahrenheit degrees:"))
print("The celsius degree is: ", convertFahrenheitToCelsius(fah))


