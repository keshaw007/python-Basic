# f=open("file2.txt", "x")
# f.close()


"""f=open("file1.txt", "r")
# print(f.read())

# \n ke karan new line character read karta hai
print(f.readline())
print(f.readline())
f.close()"""

"""f=open("file1.txt", "rb")
for line in f:
    print(line,end="")
f.close()"""


f=open("file1.txt", "rt")
content = f.read()
"""for line in f:
    print(line)
    print(line, end="")"""
# print(content)
print(content[0:10])
f.close()