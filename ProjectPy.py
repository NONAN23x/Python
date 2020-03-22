from math import sqrt
def maths():
    print(" You can choose between\nHypotenuse, Circumference, Square Root, Cube Root, Addition, Subtraction, Multiplication")
    user_input = str(input('Which Calculation do you want to make? '))
    if user_input == "Hypotenuse":
        print('Input the lengths of the shorter triangle sides')
        a = float(input('a: '))
        b = float(input('b: '))
        c = sqrt(a**2 + b**2)
        print("The length of the Hypotenuse is: %.3f" %c )
    elif user_input == "Circumference":
        Pi = 3.14
        r = float(input('Enter the radius of the circle: '))
        Area = Pi * r * r
        print('Circumference of the Circle is Defined by: %.2f' %Area)
    elif user_input == "Square Root":
        print('Input the number you want the Square root of: ')
        num1 = float(input('a: '))
        num = sqrt(num1)
        print('The Square Root of the given number is: %.2f' %num)
    elif user_input == "Cube Root":
        print('Input the number you want the cube root of: ')
        x = float(input("a: "))
        y =  x ** (1. / 3)
        print("The Cube Root of the Desired number is: %.2f" %y)
    elif user_input == "Addition":
        print('Input the numbers which you want the sum of: ')
        p = float(input('a: '))
        q = float(input('b: '))
        r = (p + q)
        print('The Sum of the Given numbers is: %.2f' %r)

    else:
        print("You Dumbhead!\n You had to Choose between Hypotenuse, Circumference, Square Root, Cube Root, Addition, Subtraction, Multiplication")

def loop_function():
    i = 1
    while i < 100:
        maths()
        user_input = str(input('Do you want to continue? (Y/N) '))
        if user_input == "Y":
            i +=1
        elif user_input == "No":
            print('Ok then Fuck Yourself')
        else:
            break
loop_function()



