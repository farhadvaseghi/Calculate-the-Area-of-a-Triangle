import math


def area_triangle(x, y, z):
    """ This function takes three sides of a triangle
        and calculate the area of triangle with Heron's formula"""
    s = (x + y + z) / 2
    area = math.sqrt(s*(s - x) * (s - y) * (s - z))
    return area


a = input("Please Enter the three sides of triangle separated with comma ")
b = a.split(sep=',')
area = area_triangle(float(b[0]), float(b[1]), float(b[2]))
print("The area of your triangle is: ", area)

