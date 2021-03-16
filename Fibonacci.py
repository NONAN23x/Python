nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto", nterms, ":")
   print(n1)
else:
   print("Fibonacci sequence:")
   for i in range(0, nterms):
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
