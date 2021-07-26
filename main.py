# Author: Kris Armstrong, CISSP
# Date: July 26, 2021
#

# This is a python script that will calculate the:
# Area of a Square or Rectangle
# Perimeter of a Square or Rectangle.


def calc_area_of_square():
    square_side = float(input("Please input value for one side: "))
    square_area = (square_side * square_side)
    print("The area of the square is: ", square_area)
    return menu()


def calc_perimeter_of_square():
    square_side = float(input("Please input value for one side: "))
    square_perimeter = (4 * square_side)
    print("The perimeter of the square is: ", square_perimeter)
    return menu()


def calc_area_of_rectangle():
    rectangle_width = float(input("Please input the width of the rectangle: "))
    rectangle_length = float(input("Please input the width of the length: "))
    rectangle_area = (rectangle_width * rectangle_length)
    print("The area of the rectangle is: ", rectangle_area)
    return menu()


def calc_perimeter_of_rectangle():
    rectangle_width = float(input("Please input the width of the rectangle: "))
    rectangle_length = float(input("Please input the width of the length: "))
    rectangle_perimeter = (2 * rectangle_width) + (2 * rectangle_length)
    print("The perimeter of the rectangle is: ", rectangle_perimeter)
    return menu()


# Menu functon which calls the appropiate math function based on the menu selection
def menu():
    print("************Welcome to Area & Perimeter Calculator**************")
    print()

    choice = input("""
                      A: Calculate the area of a square
                      B: Calculate the perimeter of a square
                      C: Calculate the area of a rectangle
                      D: Calculate the perimeter of a rectangle

                      Please enter your choice: """)

    if choice.lower() == "a":
        calc_area_of_square()
    elif choice.lower() == "b":
        calc_perimeter_of_square()
    elif choice.lower() == "c":
        calc_area_of_rectangle()
    elif choice.lower() == "d":
        calc_perimeter_of_rectangle()
    elif choice.lower() == "q":
        exit()
    elif print("please enter a valid choice"):
        menu()


# Main Function which calls the Menu Function
if __name__ == '__main__':
    menu()
