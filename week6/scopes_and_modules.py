from datetime import datetime as dt
import math as m
from geometry import circule
from geometry import rectangle
#1)
count = 0
def bump():
    global count
    count += 1
    return 
def value():
    bump()
    return count

#2)
def make_counter():
    count = 0
    def stam():
        count += 1
        return count
    return stam

#3)
x = "global"
def outer():
    x = "enclosing"
    def inner():
        4 / 5
        x = "local"
        print(x)
    inner()
    print(x)
outer()
print(x)

#4)
list = [1, 2, 3]
print(list(range(5)))

#7)
print(dt.now())
#8)
def  public_names(m):
    new_list = []
    atribut = dir(m)
    for i in atribut:
        if "_" in i:
            continue
        else:
            new_list.append(i)
    return sorted(new_list)
print(public_names(m))

#9)
def add_item(item, bag=None):
    bag.append(item)
    return bag
#10)
#print(circule.area(5))
#print(rectangle.area(4, 6))