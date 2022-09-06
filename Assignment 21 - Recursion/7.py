"""Write a recursive python function to print squares of first N natural numbers."""
def Squares(n,i=1):
    if i<n:
        print(i**2,end =' ')
        Squares(n,i+1)
x = int(input("Enter A Natutal number:"))
Squares(x)