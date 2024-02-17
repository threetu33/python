content=["小明","小红","小凡","小芳"]
year = "虎"
for name in content:
    message="""
    哈哈哈哈，哈哈哈哈。
    哈哈哈哈，哈哈哈哈。
    金{year}贺岁，哈哈哈哈。
    金{year}敲门，哈哈哈哈。
    给{name}和家人拜年啦！
    哈哈哈哈哈哈哈！""".format(year=year,name=name)
    print(message)

for name in content:
    message="""
    哈哈哈哈，哈哈哈哈。
    哈哈哈哈，哈哈哈哈。
    金{year1}贺岁，哈哈哈哈。
    金{year1}敲门，哈哈哈哈。
    给{name1}和家人拜年啦！
    哈哈哈哈哈哈哈！""".format(year1=year,name1=name)
    print(message)

for name in content:
    message="""
    哈哈哈哈，哈哈哈哈。
    哈哈哈哈，哈哈哈哈。
    金{0}贺岁，哈哈哈哈。
    金{0}敲门，哈哈哈哈。
    给{1}和家人拜年啦！
    哈哈哈哈哈哈哈！""".format(year,name)
    print(message)
#如果代表的是数字，可以在格式化时后面加：2f，保留两位浮点数
#{0；2f}

#f-字符串
for name in content:
    message=f"""
    哈哈哈哈，哈哈哈哈。
    哈哈哈哈，哈哈哈哈。
    金{year}贺岁，哈哈哈哈。
    金{year}敲门，哈哈哈哈。
    给{name}和家人拜年啦！
    哈哈哈哈哈哈哈！"""
    print(message)


