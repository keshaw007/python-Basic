with open ("file1.txt") as f:
    a=f.readlines()
    print(a)
f = open("file1.txt", "r+")
b=f.readlines()
print(b)
f.close()