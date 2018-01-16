from time import strftime, clock
from selenium.webdriver.common.keys import Keys
import requests
import sys

def open_webbrowser(browser, keywords):
    print(strftime("%Y-%m-%d %H:%M:%S") + " 打开浏览器搜索：" + keywords, flush=True)
    start = clock()
    element = browser.find_element_by_id("kw")
    element.clear()
    element.send_keys(keywords)
    element.send_keys(Keys.RETURN)
    print(strftime("%Y-%m-%d %H:%M:%S") + " 结束浏览器搜索，用时" + str(clock() - start) + "秒", flush=True)


def question_choices_count(question, choices):
    print(strftime("%Y-%m-%d %H:%M:%S") + " 计算问题与每个选项进行搜索的词条数", flush=True)
    start = clock()

    most_choice = ''
    most_val = 0
    least_choice = ''
    least_val = sys.maxsize
    for choice in choices:
        response = requests.get(url='http://www.baidu.com/s', params={'wd': question + ' ' + choice})
        begin = response.text.find('百度为您找到相关结果约') + 11
        end = response.text.find('个')
        cnt = response.text[begin:end]
        cnt = cnt.replace(',','')
        if cnt == '':
            cnt = '0'
        print(choice + '：' + cnt)
        if int(cnt) > most_val:
            most_val = int(cnt)
            most_choice = choice
        if int(cnt) < least_val:
            least_val = int(cnt)
            least_choice = choice
    
    print('*********** 1 ***********最多的是：' + most_choice)
    print('*********** 1 ***********最少的是：' + least_choice)    

    print(strftime("%Y-%m-%d %H:%M:%S") + " 结束计算，用时" + str(clock() - start) + "秒", flush=True)

def choices_count(question, choices):
    print(strftime("%Y-%m-%d %H:%M:%S") + " 计算问题包含每个选项的次数", flush=True)
    start = clock()

    most_choice = ''
    most_val = 0
    least_choice = ''
    least_val = sys.maxsize
    for choice in choices:
        response = requests.get(url='http://www.baidu.com/s', params={'wd': question})
        cnt = response.text.count(choice)
        print(choice + '：' + str(cnt))
        if cnt > most_val:
            most_val = cnt
            most_choice = choice
        if cnt < least_val:
            least_val = cnt
            least_choice = choice
    
    print('*********** 2 ***********最多的是：' + most_choice)
    print('*********** 2 ***********最少的是：' + least_choice)

    print(strftime("%Y-%m-%d %H:%M:%S") + " 结束计算，用时" + str(clock() - start) + "秒", flush=True)
