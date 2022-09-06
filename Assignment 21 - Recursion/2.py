"""Write a recursive python function to print first N natural numbers in reverse order."""
def printN(n):
    if n>0:
        print(n,end =' ')
        printN(n-1)
x = int(input("Enter a Natural numbers:"))
printN(x)
