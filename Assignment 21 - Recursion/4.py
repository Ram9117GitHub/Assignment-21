"""Write a recursive python function to print first N odd natural numbers in reverse order."""
def oddN(n):
    if n>=1:
        print((2*n)-1,end = ' ')
        oddN(n-1)
x = int(input("Enter a Natural numbers:"))
oddN(x)
