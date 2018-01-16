import unittest
import os
from PIL import Image
from context import core
from core.screenshot import capture_screen, process_image

temp_file = 'screenshot_temp.png'

class TestScreenshot(unittest.TestCase):

    def test_screenshot(self):
        capture_screen(filename=temp_file)
        img = Image.open(os.path.join('screenshots', temp_file))
        img.show()
        print('文件格式:', img.format)
        print('文件尺寸:', img.size)
        print('图片模式:', img.mode)


    def test_imagecrop(self):
        process_image(filename='screenshot_test.png')
        Image.open(os.path.join('screenshots', 'screenshot_question.png')).show()
        Image.open(os.path.join('screenshots', 'screenshot_choices.png')).show()


    def tearDown(self):
        if os.path.exists(os.path.join('screenshots', temp_file)):
            os.remove(os.path.join('screenshots', temp_file))


if __name__ == '__main__':
    unittest.main()
