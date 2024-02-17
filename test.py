#断言assert
#assert后面跟上认为正确的表达式
#会返回True False
#True无事发生  False 发生AssertionError，终止
assert 3<77


#单元测试库 unittest  内置的无需安装
import unittest
#测试代码一般放到独立的文件里


#测试代码
import unittest
from test2 import my_adder

class TestMyAdder(unittest.TeseCase):
    #一定以test_开头
    def test_1(self):
        self.assertEqual(my_adder(5,3),8)
    def test_1(self):
        self.assertEqual(my_adder(4,4),8)

#终端输入python -m unittest
#会查找所有以test_开头的相关类
#几个点代表通过了几个，F代表不通过
