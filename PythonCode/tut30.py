while(True):

    n = int(input())
    a = 8
    b = str((a >= n))
    print (b)

    if(b == "True"):
        for i in range(n):
            for j in range(n):
                if(i >= j):
                    print("* ", end="")
            print("\n")

    else:
        for i in range(n):
            for j in range(n):
                if(i <= j):
                    print("* ", end="")
            print("\n")
    print("Press'Y' or 'y' to continue program or press any other key to stop program")
    ans=input()
    if(ans=='Y' or 'y'):
        break
    else:
        continue