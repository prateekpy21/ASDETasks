"""
Task-3 Debugging
Given below is a Bash / Python script that performs following computation on an integer input (n):
If n is less than 10: Calculate its Square
Example: 4 => 16
If n is between 10 and 20: Calculate the factorial of (n-10)
Example: 15 => 120
If n is greater than 20: Calculate the sum of all integers between 1 and (n-20)
Example: 25 => 15

"""
def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        # Loop failed for n = 10 as the function start from 1 change the range(1,n-10) to range(1,(n-10)+1)
        # Also the case for n=20 is not stated taking by default that between 10 and 20 means inclusive of both 10 and 20 n<=20
        for i in range(1, (n-10)+1):
            out *= i
    else:
        lim = n - 20
        out = lim * lim
        #Wrong formula value out = out + lim as sum of n natural number is (n^2+n)/2.
        out = out + lim
        out = out / 2 
    print(out)

n = int(input("Enter an integer: "))
compute(n)


