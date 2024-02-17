#打开文件 open(相对/绝对路径，模式)
#r（可以省略） 只读 w 只写
#找不到文件FileNotFoundError
#可选：编码方式 encoding="utf-8"
f = open("./file_read.txt","r",encoding="utf-8")

#代码会记录读到哪里了
#读取所有内容并以字符串进行返回
#read会读完整个字符串，文件太大不宜使用
print(f.read())

#第二次会读空字符串
print(f.read())

#读1-10个字节的文件内容
print(f.read(10))
#读11-20个字节的文件内容
print(f.read(10))

#只读一行并打印
print(f.readline())

#常用while循环
f = open("./file_read.txt","r",encoding="utf-8")
line=f.raedline()
while line != "":
    print(line)
    line=f.readline()

#readlines读取文件全部内容，并把每行作为列表元素返回
f = open("./file_read.txt","r",encoding="utf-8")
print(f.readlines())

#readlines使用方法
f = open("./file_read.txt","r",encoding="utf-8")
lines=f.readlines()
for line in lines:
    print(line)

#关闭文件，释放资源
f.close()

#另一种关闭方法
with open("./file_read.txt","r",encoding="utf-8") as f:
    print(f.readlines())
