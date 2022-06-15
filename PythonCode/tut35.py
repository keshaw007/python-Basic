#RECURSION

n=int(input())
def fact(n):
    """This is function to calculate factorial"""
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n>1):
        return n*fact(n-1)
    elif(n<0):
        print("Factorial not possible")
# fact(n)
print(fact(n))
print(fact.__doc__)
