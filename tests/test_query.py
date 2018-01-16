import unittest
from context import core
from core.query import question_choices_count, choices_count

class TestQuery(unittest.TestCase):

    def test_question_choices_count(self):
        question = '2017年9月,导演冯小刚凭借哪部作品获得了第31届金鸡奖最佳导演奖?'
        choices = ['《我不是潘金莲》', '《私人订制》', '《芳华》']
        question_choices_count(question, choices)

    def test_choices_count(self):
        question = '2017年9月,导演冯小刚凭借哪部作品获得了第31届金鸡奖最佳导演奖?'
        choices = ['《我不是潘金莲》', '《私人订制》', '《芳华》']
        choices_count(question, choices)

if __name__ == '__main__':
    unittest.main()