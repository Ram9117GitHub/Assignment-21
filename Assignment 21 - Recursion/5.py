""" Write a recursive python function to print first N even natural numbers."""
def evenN(n,i=1):
    if i<=n:
        print(2*i,end = ' ')
        evenN(n,i+1)
x = int(input("Enter a Natural numbers:"))
evenN(x)
