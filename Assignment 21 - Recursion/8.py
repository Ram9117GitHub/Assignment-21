"""Write a recursive python function to print cubes of first N natural numbers."""
def Cubes(n,i=1):
    if i<n:
        print(i**3,end =' ')
        Cubes(n,i+1)
x = int(input("Enter A Natutal number:"))
Cubes(x)