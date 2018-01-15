import os
from PIL import Image
from aip import AipOcr

class orc(object):
    
    def __init__(self, app_id, api_key, secret_key):
        self.__client = AipOcr(appId=app_id, apiKey=api_key, secretKey=secret_key)
        self.__client.setConnectionTimeoutInMillis(5000)
    

    def get_result(self):
        options = {}
        options['language_type'] = 'CHN_ENG'

        img_question = self.__get_image_content(filename='screenshot_question.png')
        question_dist = self.__client.basicGeneral(img_question, options)
        if 'error_code' in question_dist:
            print(question_dist)
            return ''
        else:
            question = question_dist['words_result'][0]['words']
            index = question.find('.') + 1
            question = question[index:]
            # print(question)
        
        choices = []
        img_a = self.__get_image_content(filename='screenshot_a.png')
        a_dist = self.__client.basicGeneral(img_a, options)
        if 'error_code' in a_dist:
            print(a_dist)
            return ''
        else:
            a = a_dist['words_result'][0]['words']
            choices.append(a)
            # print(a)


        img_b = self.__get_image_content(filename='screenshot_b.png')
        b_dist = self.__client.basicGeneral(img_b, options)
        if 'error_code' in b_dist:
            print(b_dist)
            return ''
        else:
            b = b_dist['words_result'][0]['words']
            choices.append(b)
            # print(b)

        img_c = self.__get_image_content(filename='screenshot_c.png')
        c_dist = self.__client.basicGeneral(img_c, options)        
        if 'error_code' in c_dist:
            print(c_dist)
            return ''
        else:
            c = c_dist['words_result'][0]['words']
            choices.append(c)
            # print(c)
        
        return question, choices


    def __get_image_content(self, filename='screenshot.png'):
        with open(os.path.join('screenshots', filename), 'rb') as fp:
            return fp.read()

