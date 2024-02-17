#类命名风格 Pascal命名法
#用字母大写来分割单词
#如UserAccount  CustomerOrder

#定义属性示例
class CuteCat:
    def __init__(self):
        self.name="Dale"
        

cat1=CuteCat()
print(cat1.name)

#并非所有猫都叫Dale
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name=cat_name
        self.color=cat_color
        self.age=cat_age
        

cat1=CuteCat("Dale",3,"pink")
print(cat1.name)
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")


#定义方法示例
#和定义函数有两点不同
#1.要放在类里面
#2.第一个参数被占用是self
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name=cat_name
        self.color=cat_color
        self.age=cat_age
    def speak(self):
        print("喵"*self.age)
    def think(self,content):
        print(f"小猫{self.name}在思考{content}...")

cat1.speak()
cat1.think("现在要不要去抓老鼠呢？")