#写的模式下文件不存在会自动创建
#会清空原本的内容
#不会自动换行
with open("./file_write.txt","w",encoding="utf-8") as f:
    f.write("hello\n")
    f.write("hi")

#不清空，追加内容
#文件不存在也会创建一个
with open("./file_write.txt","a",encoding="utf-8") as f:
    f.write("hello")

#a,w都不能读
#同时读写 r+
with open("./file_write.txt","r+",encoding="utf-8") as f:
    print(f.read)
    #此时以追加的形式写入文件
    f.write("hello")