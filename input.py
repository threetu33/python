a=input("请输入您的年龄：")

print("你的年龄是"+a+"岁")
#input全会返回字符串
#所以不能直接进行运算
#如print(a+2)

#int可以把其他类型变为整数
#floor可以把其他类型变为浮点数
#str可以把其他类型变为字符串

#int用法
int("66666")

#整数不能直接加字符串，需要转换类型
print("你今年"+str(2)+"岁")

user_age=int(input("你的年龄是："))
user_age_after_ten_years=user_age=10
print("您十年后的年龄是"+str(user_age_after_ten_years)+"岁")