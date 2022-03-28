# This program computes the area of a triangle
# using the Heron's formula

import math

# enter input (separated by spaces):
# try: 3 4 5
# try: 1 3 5
input_string = input( "Enter the sides of the triangle: ")
a, b, c = map(float, input_string.split())

# do calculations
p =  a + b + c
s = 0.5 * p
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

# print results
print()
print("%20s %0.2f" % ("Side A: ", a))
print("%20s %0.2f" % ("Side B: ", b))
print("%20s %0.2f" % ("Side C: ", c))
print("%20s %0.2f" % ("Perimeter: ", p))
print("%20s %0.2f" % ("Area: ", area))


# TODO
# - Try the sides 2, 5, 3 and the sides 1, 5, 3. How to fix it?
# - Compute the angles between sides in degrees and print them.