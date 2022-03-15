from cmath import pi, sqrt

print("------ Calculate the area of shapes! -----")

#Selection of shapes:
shape = input("Enter shape: \n 'r' = rectangle \n 'c' = circle \n 's' = square \n 't' = triangle \n 'h' = hexagon \n here: ")
if shape == "r":
    height = input("Insert height: ")
    length = input("Insert length: ")
    area = int(height) * int(length)
    print("Area: " + str(area))
    print("Done")
if shape == "c":
    radius = input("Insert radius: ")
    area = 2*pi*int(radius)
    print("Area: " + area)
    print("Done")
if shape == "s":
    length = input("Insert length: ")
    area = int(length)**2
    print("Area: " + str(area))
    print("Done")
if shape == "t":
    height = input("Insert height: ")
    base = input("Insert base size: ")
    area = (int(height) * int(base))/2
    print("Area: " + str(area))
    print("Done")
if shape == "h":
    side_length = input("Insert side length: ")
    area_part1 = ((3*(sqrt(3)))/2)
    area1_real = area_part1.real
    area = area1_real * (int(side_length))**2
    print("Area: " + str(area))
    print("Done")