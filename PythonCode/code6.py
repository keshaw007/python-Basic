def fibonacii(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    if(n>1):
        return fibonacii(n-1) + fibonacii(n-2)
num=int(input())
i=1
while i<=num:
    if(i==1):
        print("series is")
    if(i>1 and i<=num):
        print("+", end=" ")
    print(fibonacii(i),end=" ")
    i=i+1
print("\n",num,"th term of fibonacii series is ", fibonacii(num))