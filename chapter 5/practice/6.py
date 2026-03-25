'''Check triangle type'''

sides = [int(side) for side in input("Enter triangle side seprated by space : ").split()]

side1 = sides[0]
side2 = sides[1]
side3 = sides[2]


if side1 == side2 and side2 == side3 and side1 == side3:
    print("The triangle is a Equilateral triangle")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is a isosceles triangle")

else:
    print("The triangle is a Scalene triangle")




