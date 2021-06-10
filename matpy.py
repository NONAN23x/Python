#!/bin/python3

# Importing the important libraries
import random
import numpy as np
import time
import colorama
import os

# defining how to interpret colors
cyan = colorama.Fore.CYAN
green = colorama.Fore.GREEN
black = colorama.Fore.BLACK
blue = colorama.Fore.BLUE
red = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
light_black = colorama.Fore.LIGHTBLACK_EX
light_magenta = colorama.Fore.LIGHTMAGENTA_EX
light_red = colorama.Fore.LIGHTRED_EX
light_green = colorama.Fore.LIGHTGREEN_EX
light_cyan = colorama.Fore.LIGHTCYAN_EX
finish = colorama.Style.RESET_ALL

# Defining a list to use them all at once
colors = [cyan, green, blue, red, yellow, light_green, light_cyan, light_magenta, light_black, light_red]

#Banner design
def banner():
    os.system("clear")
    time.sleep(0.5)
    print(random.choice(colors), "\n      ###    ###   ###      ")
    print("     ~MATRIX CALCULATOR~       (https://github.com/NONAN23x)")
    print("      ###    ###   ###         (author: NONAN23x) \n\n", finish)

    time.sleep(0.35)
    print(random.choice(colors), "Select the type of operation you would like :)\n")
    print("     [1] Inverse of a matrix\n")
    print("     [2] Determinant of a matrix\n")
    print("     [3] Rank of a matrix\n")
    print("     [4] Transpose of a matrix\n")
    print("     [5] Trace of a matrix\n", finish)


banner()
try:
    user_selection = int(input("----: "))
    if user_selection == 1:
        choice = "inverse"
    elif user_selection == 2:
        choice = "determinant"
    elif user_selection == 3:
        choice = "rank"
    elif user_selection == 4:
        choice = "transpose"
    elif user_selection == 5:
        choice = "trace"
except:
    print("Your option didn't matach the available options, exiting:)")
    exit()

try:
    print(random.choice(colors), " \nI will carry out the mathematics, but I need a matrix to work on,\n "
          "please fill out the respective positions as follows\n")
    print(np.array([["a11", "a12", "a13"], ["a21", "a22", "a23"], ["a31", "a32", "a33"]]))
    print()
    a11 = int(input("a11 = "))
    a12 = int(input("a12 = "))
    a13 = int(input("a13 = "))
    a21 = int(input("a21 = "))
    a22 = int(input("a22 = "))
    a23 = int(input("a23 = "))
    a31 = int(input("a31 = "))
    a32 = int(input("a32 = "))
    a33 = int(input("a33 = "))

    answer_list = [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]

    print("\nThe given matrix:")
    matrix = np.array(answer_list)
    print(matrix)
    print(f"\nAnd the {choice} is:\n", finish)
    if user_selection == 1:
        print(np.linalg.inv(matrix))
    elif user_selection == 2:
        print(int(np.linalg.det(matrix)))
    elif user_selection == 3:
        print(np.linalg.matrix_rank(matrix))
    elif user_selection == 4:
        print(np.transpose(matrix))
    elif user_selection == 5:
        print(np.trace(matrix))
except:
    print(red, "Program Interrupted :(", finish)
