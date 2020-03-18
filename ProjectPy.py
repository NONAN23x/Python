print('\n\nHello User,\nThis application is under development so dont expect anything so flashy')
print('Go ahead and type what command you would like to run\n')
a = "Addition"
b = "Subratction"
c = "Multiplication"
d = "Division\n"
Functions = [a,b,c,d]
print(Functions[0],',',Functions[1],',',Functions[2],',',Functions[3])
x = (input(':'))
y = len(x)
if y == len(a):
    print('Adding the given Numbers')
    print (float(input('1:')) + float(input('2: ')))
if y != len(a):
    exit()
if y == len(b):
    print('Subtracting the given Numbers')
    print(float(input('1:')) - float(input('2: ')))