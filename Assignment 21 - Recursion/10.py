"""Write a recursive python function to print a number in reverse order"""
def PrintN(n):
    if n>=0:
        print(n,end =' ')
        PrintN(n-1)
x = int(input("Enter a Natural numner:"))
PrintN(x)