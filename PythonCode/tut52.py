"""def func1(num):
    if(num==0):
        return print
    else:
        return sum
a=func1(0)
b=func1(1)
print(a)
print(b)"""

"""def func1(func2):
    func2(3*4)
func1(print)"""

import pdb
def dec1(func1):
    def nowexe():
        print("executing now")
        func1()
        print("executed")
    return nowexe
"""def hero():
    print("I am a HERO")
hero=dec1(hero)
hero()"""


@dec1
def hero():
    print("I am a HERO")
hero()
