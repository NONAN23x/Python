import time
indent = 0
indentIncreasing = True
left = True
right = 2
middle = 0

while True:
    print(' ' * indent, end='')
    print("HHTTHH")
    time.sleep(0.24)
    if left:
        indent = 0
        right += 1
        if right == 10:
            right = 2
            left = False
    else:
        indent = 5
        middle = middle + 5
        if middle == 60:
            left = True
            middle = 0
