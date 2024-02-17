#unittest库里有许多针对方法
#assertTrue万能但推荐用针对方法
#针对方法报错解释更详细

import unittest
from sentence import Sentence
#unittest库里的setUp可以避免重复创建类
class TestSentence(unittest.TestCase):
    def setUp(self):
        self.sentence = Sentence("hello world")
    
    def test_str_count(self):
        self.assertEqual(self.sentence.str_count(),12)

    def test_word_count(self):
        self.assertEqual(self.sentence.word_count(),2)

#针对函数
# assertEqual(A,B)  assertA==B
# assertTrue(A)     assert A is True
# assertin(A,B)     assert A in B
# assertNotEqual(A,B)  assert A != B
# assertFalse(A)       assert A is False
# assertNotln(A,B)     assert A not in B