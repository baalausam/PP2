import math

sides = int(input("Enter number of sides: "))
length = float(input("Enter side length: "))
area_polygon = (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))
print("Polygon area:", round(area_polygon))