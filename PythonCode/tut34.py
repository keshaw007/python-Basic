#SCOPE OF VARIABLES
#LOCAL Vs VARIABLES

"""#LOCAL VARIABLE
def sum():
    a=10
    b=20
    sum=a+b
    print(sum)
# print(a)
sum()"""

"""# GLOBAL VARIABLE
b=10
def print_number():
    a=b+1
    print(a)
print_number()"""

"""a=20
def func():
    # a=10
    global a
    a=a+50
    print(a)
func()"""

a=10
def func():
    global a
    a=501
print("before calling function ", a)
func()
print("after calling function " ,a)