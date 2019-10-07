''' 
Transform each of the program from last week into a stand alone function.
One function caculateMpg

By: Quanyi wang

'''
from library import calculateMpg

miles = float(input("please enter miles driven:"))
gallons = float(input("please enter gallons used:"))
print("Your MPG is:", calculateMpg(miles,gallons))

