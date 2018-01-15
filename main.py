from core.orc import orc
from core.screenshot import capture_screen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import strftime, clock

browser = webdriver.Chrome(r'.\utils\chromedriver.exe')
browser.get('https://www.baidu.com')

while True:

    go = input('输入回车继续运行,输入 n 回车结束运行: ')
    if go == 'n':
        break

    print(strftime("%Y-%m-%d %H:%M:%S") + " 开始答题", flush=True)
    start = clock()

    capture_screen()

    o = orc(app_id='10689024', api_key='ABTXXPeylq1B6cUp0CdDoxlP', secret_key='dnuV0MfxVI9xIZtewfdA3qutGTPAflzS')

    question, choices = o.get_result()
    keyword = question + ' '
    for s in choices:
        keyword = keyword + s + ' '

    print(strftime("%Y-%m-%d %H:%M:%S") + " 开始搜索", flush=True)
    print(keyword)
    elem = browser.find_element_by_id("kw")
    elem.clear()
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)
    print(strftime("%Y-%m-%d %H:%M:%S") + " 结束搜索", flush=True)
    cnt = clock() - start
    print(strftime("%Y-%m-%d %H:%M:%S") + " 结束答题，用时" + str(cnt) + "s", flush=True)

    print('----------------------------------')