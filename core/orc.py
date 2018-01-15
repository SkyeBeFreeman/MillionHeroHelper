import os
from PIL import Image
from aip import AipOcr
from time import strftime

class orc(object):
    
    def __init__(self, app_id, api_key, secret_key):
        self.__client = AipOcr(appId=app_id, apiKey=api_key, secretKey=secret_key)
        self.__client.setConnectionTimeoutInMillis(3000)
    

    def get_result(self):
        print(strftime("%Y-%m-%d %H:%M:%S") + " 开始识别", flush=True)
        options = {}
        options['language_type'] = 'CHN_ENG'

        # 获取问题
        img_question = self.__get_image_content(filename='screenshot_question.png')
        question_dist = self.__client.basicGeneral(img_question, options)
        if 'error_code' in question_dist:
            print(question_dist)
            return '', ''
        else:
            question = ''
            for pair in question_dist['words_result']:
                question = question + pair['words']
            index = question.find('.') + 1
            question = question[index:]
            # print(question)
        
        # 获取选项
        choices = []
        img_choices = self.__get_image_content(filename='screenshot_choices.png')
        choices_dist = self.__client.basicGeneral(img_choices, options)        
        if 'error_code' in choices:
            print(choices)
            return '', ''
        else:
            for pair in choices_dist['words_result']:
                choices.append(pair['words'])
            # print(c)
        
        print(strftime("%Y-%m-%d %H:%M:%S") + " 识别结束", flush=True)
        return question, choices


    def __get_image_content(self, filename='screenshot.png'):
        with open(os.path.join('screenshots', filename), 'rb') as fp:
            return fp.read()

