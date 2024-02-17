#嵌套/多条件语句
a=int(input("输入你的年龄："))
if a>=50:
    if a>=75:
        print("winter")
    else:
        print("autumn")
elif a<=25:
    print("spring")
else:
    print("summer")

#如果满足多个elif，则只执行最上面一个
#python中可以使用 55<a<56 C++不能