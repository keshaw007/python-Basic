"""items=[1,2,3,4,5]
a=list(map((lambda x:x**10),items))
print(a)"""

a=[2,3,"map", "cold", 5, 9, 13]
b=["map", 0,1,15,13,9]
c=list(filter(lambda x: x in a,b))
print(c)