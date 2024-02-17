#key和value一一对应
contacts={"nvpy":13596680032,
          "mother":18340268227,
          "father":13190260777}

#key的类型一定不可变

#元组tuple不可变
contacts_2={
    ("nvpy",1):11111,
    ("nvpy",2):22222,
    ("nvpy",3):33333
}

#dictionary可变
#dictionary增加一个
contacts_2[("nvpy",4)]=44444
#更新/覆盖一个值
contacts_2[("nvpy",4)]=55555

#查找某个值是否存在
#存在返回True 不存在返回False
print("nvpy" in contacts)
print("nvpyy" in contacts)

#删除一个键值对
del contacts["nvpy"]

#查看有多少键值对
len(contacts)