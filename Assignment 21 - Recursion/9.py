"""Write a recursive python function to print first N multiples of a given number."""
def MultiplesN(n,N):
    if N<n:
        print(N*n)
        MultiplesN(n,n+1)
x = int(input("Enter A natural number: "))
mul = int(input("Enter a Multiples:"))
MultiplesN(x,mul)  
