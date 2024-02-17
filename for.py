#可以对字典，列表，字符串进行迭代
#for 变量名 in 可迭代对象：
age_list=[20,54,55,88,79,77]
for age in age_list:
    if age>=75:
        print (age)
        print ("winter")

age_dict={"1":20,"2":54,"3":55,"4":99}
age_dict.keys()  #所有键
age_dict.values()  #所有值
age_dict.items()  #所有键值对

for name,aage in age_dict():
    if aage>30:
        print (name)
        print (aage)
        print ("not spring")

#等效写法
for age_tuple in age_dict():
    name = age_tuple[0]
    aage = age_tuple[1]
    if aage>30:
        print (name)
        print (aage)
        print ("not spring")