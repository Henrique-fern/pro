#Paint area calculator
import math

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    number_of_cans = (math.ceil(number_of_cans))

    print(f"You will need {number_of_cans} cans of paint!")

paint_calc(test_h, test_w, coverage)