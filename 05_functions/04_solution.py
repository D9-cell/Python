import math

def circle_stats(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area,circumference

a,circum = circle_stats(5)
area = round(a,2)
circumference = round(circum,2)
print("Area : ",area,", Circumference : ",circumference)