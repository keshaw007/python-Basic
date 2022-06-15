n = int(input())
a = []
i = 0
while(i < n):
    a.append(int(input()))
    i = i+1
a.sort()
# print(n)
j = n-1
while(j>=0):
    if a[j] > a[j-1]:
        print(a[j-1])
        break
    else:
        j=j-1