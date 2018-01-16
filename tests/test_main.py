from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import strftime, clock
from context import core
from core.orc import orc
from core.screenshot import process_image
import configparser
import win32gui
import sys, os
from pyhooked import Hook, KeyboardEvent

def runner():
    print(strftime("%Y-%m-%d %H:%M:%S") + " 开始答题", flush=True)
    start = clock()

    process_image()

    o = orc(app_id=app_id, api_key=api_key, secret_key=secret_key)

    question, choices = o.get_result()
    keyword = question + ' '
    for s in choices:
        keyword = keyword + s + ' '

    print(strftime("%Y-%m-%d %H:%M:%S") + " 开始搜索：" + keyword, flush=True)
    elem = browser.find_element_by_id("kw")
    elem.clear()
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)
    print(strftime("%Y-%m-%d %H:%M:%S") + " 结束搜索", flush=True)
    cnt = clock() - start
    print(strftime("%Y-%m-%d %H:%M:%S") + " 结束答题，用时" + str(cnt) + "秒", flush=True)
    print('--------------------按C继续运行,按Q结束运行---------------------')    
    print()


def handle_events(args):
    if isinstance(args, KeyboardEvent):
        if args.current_key == 'C' and args.event_type == 'key down':
            runner()
        elif args.current_key == 'Q' and args.event_type == 'key down':
            browser.quit()
            hook.stop()
            os.exit()

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config/config.conf')
    app_id = config.get('config', 'app_id')
    api_key = config.get('config', 'api_key')
    secret_key = config.get('config', 'secret_key')

    browser = webdriver.Chrome(r'.\utils\chromedriver.exe')
    browser.get('https://www.baidu.com')

    vm = win32gui.FindWindow(None, '夜神模拟器')
    if vm <= 0:
        print('未启动夜神模拟器')
        while vm <= 0:
            vm = win32gui.FindWindow(None, '夜神模拟器')
    print('--------------------按C继续运行,按Q结束运行---------------------')
    hook = Hook()
    hook.handler = handle_events
    hook.hook()