import time
value = 0
condition = True
time.sleep(1)
print("Looper by Nonan23x;)")
user_choice = str(input("Enter the word : "))
while True:
    print(" " * value, end="")
    print(user_choice)
    time.sleep(0.01)
    if condition:
        value = value + 1
        if value == 7:
            condition = False
    else:
        value = value - 1
        if value == 0:
            condition = True
