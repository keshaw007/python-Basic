f=open("file1.txt", "r")
"""a=f.readline()
print(a)
print(f.tell())"""

f.seek(20)
print(f.readline())
print(f.readline())
f.close()