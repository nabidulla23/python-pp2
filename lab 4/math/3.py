import math
# Write a Python program to calculate the area of regular polygon.


n = int(input())

lenght = int(input())

area = (n*(math.pow(lenght, 2)))/(4*(math.tan(math.pi/n)))

print(area)


# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

