import random, time

print('Starting game\n')
time.sleep(2)
secnum = random.randint(1,20)
print("I've taken a number bwtween 1 and 20...\n")

def game():
    for i in range(1, 10):
        print('\nCan you huess that number?\n')
        print('---------->')
        guessnum = int(input())
        if guessnum < secnum:
            print('\nAim higher...')
        elif guessnum > secnum:
            print('\nAim lower...')
        else:
            break

    if guessnum == secnum:
        time.sleep(2)
        print('Correct!!!')
        print("But you took you " + str(i) + " tries to guess...")
    else:
        print('Nope the number i am thinking ois' + str(secnum))

def looping():
    game()
    print('Wanna play again?\n    (y) or (n)')
    des = input()
    if des == "y":
        game()
    elif des == "n":
        quit()
    else:
        print('Quitting')
        time.sleep(2)
        quit()


looping()
