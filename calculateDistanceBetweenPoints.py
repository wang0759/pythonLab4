'''
Write a function calculateDistanceBetweenPoints that calculates the distance
between 2 points with coordinates (x,y) and (x1,y1),
the function receives 4 paramaters: x, y, x1 and y1, all integers.
The function returns the distance between the two points.
The function must be properly tested using a main program that calls it.
Once tested, move the function into your library file.

'''

import library

x = int(input('Enter x: '))
y = int(input('Enter y: '))
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))

print('The distance between two points is: ', calculateDistanceBetweenPoints(x,y,x1,y1))

