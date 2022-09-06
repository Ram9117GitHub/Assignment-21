"""Write a recursive python function to print first N natural numbers. """
def printN(n):
    if n>1:
        printN(n-1)
        print(n,end=" ")
x = int(input("Enter a Natural numbers:"))
printN(x)
