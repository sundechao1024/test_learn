import unittest
import pytest
import allure
class TestDemo(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("执行所有用例之前要执行的类")

    @classmethod
    def tearDownClass(cls):
        print("执行所有用例之后要执行的类")

    def test_abc(self):
        print("test_abc")

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')


    def test_isupper(self):
        self.assertTrue('F00'.isupper())
        self.assertFalse('Foo'.isupper())




if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(TestDemo('test_abc'))
    unittest.TextTestRunner().run(suit)