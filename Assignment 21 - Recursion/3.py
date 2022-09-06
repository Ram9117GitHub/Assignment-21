"""Write a recursive python function to print first N odd natural numbers."""
def oddN(n,i=1):
    if i<=n:
        print((2*i)-1)
        oddN(n,i+1)
x = int(input("Enter a Natural number:"))
oddN(x)
    
