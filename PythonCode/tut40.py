"""#Method 1 but having limitation
name="keshaw"
n="My name is %s"%name
print(n)"""

"""#method 2 but having limitation
name = "keshaw"
branch = " computer science engineering"
semester = 3
print("name is %s from branch %s in semester %d"%(name,branch,semester))"""

"""#method 3 .str format
str="This article is written in {}"
print(str.format("python"))"""

"""#method 4 most relevant and latest method
str1="python"
str2="programming"
print(f"welcome to  {str1}  {str2}")"""

import math
me="keshaw"
a1=3
a="this is %s %s"%(me,a1)
# a="This is {1} {0}"
"""b=a.format(me,a1)
print(b)"""
a=f"this is {me} {a1} {math.cos(0)}"
print(a)