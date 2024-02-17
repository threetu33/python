#while 条件A： 行动B（转到下一行缩进）
#while 和 for 许多时候可以相互转换
list1 = ["a","b","c","d","e"]
for char in list1:
    print(char)


for i in range(len(list1)):
    print(list1[i])


a=0
while a < len(list1):
    print(list1[a])
    a=a+1