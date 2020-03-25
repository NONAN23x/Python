from math import sqrt
print('\nWelcome to my calculator bot.\nHere you can solve your math problems...')
print('\nPlease choose between the following: ')

def maths():
    user_input = str(input('\nWhich Calculation do you want to make?:\n    Hypotenuse, Circumference, Square Root, Kinetic energy '
                           'Cube Root, Addition, Multiplication, Division.\n '))

    if user_input == "Hypotenuse":
        print('\nInput the lengths of the shorter triangle sides:')
        a = float(input('A: '))
        b = float(input('B: '))
        c = sqrt(a**2 + b**2)
        print("The length of the Hypotenuse is: %.2f" %c )

    elif user_input == "None":
        print('Why none?\nYou want to solve your problems right?')

    elif user_input == "Circumference":
        Pi = 3.14
        r = float(input('Enter the radius of the circle: '))
        Area = Pi * r * r
        print('Circumference of the circle is Defined by: %.1f' %Area)

    elif user_input == "Square Root":
        print('Input the number you want the Square root of: ')
        num1 = float(input('\nA: '))
        num = sqrt(num1)
        print('The Square Root of the given number is: %.3f' %num)

    elif user_input == "Cube Root":
        print('Input the number you want the cube root of: ')
        x = float(input("\nA: "))
        y =  x ** (1. / 3)
        print("The Cube Root of the Desired number is: %.2f" %y)

    elif user_input == "Addition":
        print('Input the numbers which you want the sum of: ')
        p = float(input('\na: '))
        q = float(input('b: '))
        r = (p + q)
        print('The Sum of the Given numbers is: %.0f' %r)

    elif user_input == "maha pagal":
        print('Tu hunga pagal!!!')
        exit()

    elif user_input == "Subtraction":
        print('Enter the Values you want the differnce of: ')
        e = float(input('\na: '))
        f = float(input('b: '))
        g = (e - f)
        print('The Difference between the given numbers is: %.2f' %g)

    elif user_input == "Multiplication":
        print('Enter the numbers you want the product of:')
        j = float(input('\na: '))
        k = float(input('b: '))
        i = (j*k)
        print('The product of the numbers is: %.2f' %i)

    elif user_input == "Division":
        print('Enter the numbers you want the division of: ')
        l = float(input('\nA: '))
        m = float(input('b: '))
        n = (l/m)
        print('The divion of given numbers is: %.3f' %n)

    elif user_input == "Kinetic energy":
        print('What is the mass and velocity of the particle?')
        q = float(input('\nMass: '))
        w = float(input('Velocity: '))
        s = (1/2 * q * w * w)
        print('The Kinetic energy resolved is: %.1f' %s)

    else:
        print("You Dumbhead!\n You have to Choose between Hypotenuse, Circumference, Square Root, Cube Root, Addition, Subtraction, Multiplication")

def loop_function():
    i = 1
    while i < 100:
        maths()
        user_input = str(input('Do you want to continue? (Y/N) '))
        if user_input == "Y":
            i +=1
        elif user_input == 'y':
            i +=1
        elif user_input == 'n':
            break
        elif user_input == "No":
            print('\n\nOk then Fuck Yourself')
            exit()
        else:
            break

loop_function()