x=88
def func1():
    x=20
    def func2():
        global x
        x=56
    func2()
func1()
print(x)