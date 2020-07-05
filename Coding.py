import time  # imports the time module
iterations = int(input("How many iterations? = "))  # asks the user how long does he wants the list to be
times = range(iterations)
create_alist = []  # an empty list where each answer is added
for i in times:  # a for loop for iterations
    number = float(input("Enter the number :  "))
    power = float(input("Enter the power : "))
    answers = number ** power
    time.sleep(0.25)  # just for show
    create_alist.append(answers)
for i in create_alist:
    print(i)  # finally, the answers are printed line by line