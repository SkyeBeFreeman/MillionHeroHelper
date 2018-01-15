import unittest
import os
from PIL import Image
# from core.screenshot import capture_screen
from context import core
from core.orc import orc

temp_file = 'screenshot_temp.png'

class TestORC(unittest.TestCase):

    def setUp(self):
        self.o = orc(app_id='10689024', api_key='ABTXXPeylq1B6cUp0CdDoxlP', secret_key='dnuV0MfxVI9xIZtewfdA3qutGTPAflzS')

    def test_get_result(self):
        question, choices = self.o.get_result()
        print(question)
        print(choices)

    # def tearDown(self):


if __name__ == '__main__':
    unittest.main()
