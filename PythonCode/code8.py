a=list(input())
c=a.__len__()
if '1' in a:
    b=a.index('1')
    print(b)
    for i in range(b+1,c):
        a[i]='0';
    print((str(a)))
else:
    print("0")