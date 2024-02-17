class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name=cat_name
        self.color=cat_color
        self.age=cat_age
    def speak(self):
        print("喵"*self.age)
    def think(self,content):
        print(f"小猫{self.name}在思考{content}...")

#括号里写上父类的名字
class CuteCat1(CuteCat):
    def read(self):
        print(self.name+" is reading")


#有优先看所属类有无方法，若无看父类
cat1=CuteCat1()
cat1.read()

#super().__init__会调用父类的
class CuteCat2(CuteCat):
    def __init__(self,cat_name,cat_age,cat_color,tail):
        super().__init__(cat_name,cat_age,cat_color)
        self.tail=False

