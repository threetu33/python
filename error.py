#ImportError引入错误
#ArithmeticError计算错误
#ZeroDivisionError除零错误
#KeyError键错误
#ValueError值错误
#SyntaxError语法错误
#IndentationError缩进错误
#IndexError索引错误


#try except语句捕捉异常
#捕捉错误从上往下运行
weight=float(input("your weight is "))
height=float(input("your height is "))
BMI=weight/height**2

try:
    weight=float(input("your weight is "))
    height=float(input("your height is "))
    BMI=weight/height**2
except ValueError:
    print("输入为不合理数字，请重新运行程序，并输入正确的数字")
except ZeroDivisionError:
    print("身高不能为0,请重新运行程序，并输入正确的数字")
except:
    print("发生了未知错误，请重新运行程序")

#不产生错误时运行的程序
else:
    print("BMI="+str(BMI))

#无论错误与否都运行的程序
finally:
    print("程序运行结束。")