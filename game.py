import random, time

def game():
    secnum = random.randint(1,20)
    print('Starting game\n')
    time.sleep(0.5)
    print("I've chosen a number bwtween 1 and 20...\n")
    for i in range(1, 10):
        print('\nGuess the number.\n')
        print('----># ')
        guessnum = int(input())
        if guessnum < secnum:
            print('\nAim higher...')
        elif guessnum > secnum:
            print('\nAim lower...')
        else:
            break

    if guessnum == secnum:
        time.sleep(0.5)
        print('Correct!!!')
        print("Thats with a total of " + str(i) + " tries")
    else:
        print('Failed.\nThe number was: ' + str(secnum))

    return None
game()
