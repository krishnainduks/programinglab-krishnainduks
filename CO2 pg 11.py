#Write lambda functions to find area of square, rectangle and triangle. 

import math

t_area = lambda b,h : 1/2*b*h
r_area = lambda l,b : l*b
s_area = lambda a : a*a

print("Area of Triangle :", t_area(20,30))
print("Area of Rectangle:", r_area(20,10))
print("Area of Square :", s_area(12))