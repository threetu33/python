import math

#求和函数
sum([1,2,11])

#定义新函数
def s(a,b):
    a=float(input("半径为："))
    b=float(input("圆心角为："))
    s=b/360*math.pi*a**2
    print("面积为"+str(s))

#调用函数
s()

#return
def s(a,b):
    a=float(input("半径为："))
    b=float(input("圆心角为："))
    s=b/360*math.pi*a**2
    print("面积为"+str(s))
    return s

#调用s的值
aa=s()