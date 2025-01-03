# Write a program that accepts the lengths of three sides of a triangle as inputs and outputs whether or not the triangle is a right triangle

# def right_triangle(a,b,c):
#     sides = sorted([a,b,c])
#     return sides[0]**2 + sides[1]**2 == sides[2]**2
# a = float(input("Enter the length of the first side: "))
# b = float(input("Enter the length of the second side: "))
# c = float(input("Enter the length of the third side: "))
#
# if right_triangle(a,b,c):
#     print("The triangle is right angle triangle. ")
# else:
#     print("The triangle is not a right angle triangle.")

def is_right_angle(a,b,c):
    sides = sorted([a,b,c])
    hypotenuse = sides[-1]
    other_sides = sides[:-1]
    return hypotenuse**2 == other_sides[0]**2 + other_sides[1]**2

while True:
    try:
        a = float(input("enter the length of side A: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c "))

        if a <= 0 or b <= 0 or c <=0:
            raise ValueError("All sides of a triangle must be positive..")
        break
    except ValueError as e:
        print(e)
        print("Pls enter valid positive numbers..")

if is_right_angle(a,b,c):
    print("The triangle is right triangle.")
else:
    print("The triangle is not a right triangle.")

