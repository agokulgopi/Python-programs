from curses.textpad import rectangle


def area_of_rectangle(length,width):
    area = length * width
    return area

message = "This message is accessible throughout the program."

rectangle_length = int(input("Enter the length: "))
rectangle_width = int(input('Enter the width: '))

rectangle_area = area_of_rectangle(rectangle_length,rectangle_width)

print(f'Area of rectangle= {rectangle_area}')