#引入模块
#引入统计模块
import statistics

#第二种方法
#好处：之后调用函数不需要写模块名
from statistics import median,mean

#第三种方法
#所有都不需要带模块名
#不推荐，容易名字冲突
from statistics import *

#ctrl+函数名可查看源代码（windows）
#引用模块需要先安装 （在终端） pip install
#可以在官网查找第三方库 
#网址：pypi.org