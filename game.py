import random, time
print()
print('System_Generic Rebooting...\n')
k = 10
time.sleep(3)
secnum = random.randint(1,20)
print('I have taken a number, not less than 1 and not greater than 20...\n ')
time.sleep(2)


for i in range(1,10):
    print('Can you guess that number???\n')
    guess = int(input('----->\n '))

    if guess < secnum:
        time.sleep(2)
        print('Nope aim higher...')
    elif guess > secnum:
        time.sleep(2)
        print('\nWhat? Aim a little bit smaller')
    else:
        break

if guess == secnum:
    time.sleep(2)
    print('\nYup, you do have brain...\n')
    time.sleep(2)
    print('But it took ' + str(i) + " tries for your brain to function...")
else:
    time.sleep(2)
    print('Nope, the number i was thinking was actually ' + str(secnum))
