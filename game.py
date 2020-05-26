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
    i = 1
    while i < 100:
        game()
        secnum = 0
        des = input("Do you want to continue? (y) or (n) ")
        if des == "y":
            i += 1
        elif des == "n":
            break
            quit()
        else:
            print(" Exiting... ")
            
            
        



looping()
