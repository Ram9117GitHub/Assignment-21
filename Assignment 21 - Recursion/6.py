"""Write a recursive python function to print first N even natural numbers in reverse order."""
def evenN(n,i=1):
    if i<=n:
        evenN(n,i+1)
        print(2*i,end = ' ')
x = int(input("Enter a Natural numbers:"))
evenN(x)