import unittest
import sys, os
sys.path.append('..\\..')
from PIL import Image
# from core.screenshot import capture_screen
from context import core
from core.screenshot import capture_screen

temp_file = 'screenshot_temp.png'

class TestScreenshot(unittest.TestCase):
    def test_screenshot(self):
        
        capture_screen(filename=temp_file)
        img = Image.open(os.path.join('screenshots', temp_file))
        img.show()
        print('文件格式:', img.format)
        print('文件尺寸:', img.size)
        print('图片模式:', img.mode)


    def tearDown(self):
        os.remove(os.path.join('screenshots', temp_file))

if __name__ == '__main__':
    unittest.main()