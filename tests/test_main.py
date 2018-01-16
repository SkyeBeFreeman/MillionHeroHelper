from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import strftime, clock
from context import core
from core.orc import orc
from core.screenshot import process_image
from core.query import open_webbrowser, question_choices_count, choices_count
import configparser
import win32gui
import sys, os
from pyhooked import Hook, KeyboardEvent
from threading import Thread

def runner():
    print(strftime("%Y-%m-%d %H:%M:%S") + " 开始答题", flush=True)
    start = clock()

    process_image(filename='screenshot_test.png')

    o = orc(app_id=app_id, api_key=api_key, secret_key=secret_key)

    question, choices = o.get_result()

    keywords = question + ' '
    for s in choices:
        keywords = keywords + s + ' '

    Thread(choices_count(question, choices)).start()
    Thread(question_choices_count(question, choices)).start()
    Thread(open_webbrowser(browser, keywords)).start()

    cnt = clock() - start
    print(strftime("%Y-%m-%d %H:%M:%S") + " 结束答题，用时" + str(cnt) + "秒", flush=True)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config/config.conf')
    app_id = config.get('config', 'app_id')
    api_key = config.get('config', 'api_key')
    secret_key = config.get('config', 'secret_key')

    browser = webdriver.Chrome(r'.\utils\chromedriver.exe')
    browser.get('https://www.baidu.com')

    runner()

    browser.quit()