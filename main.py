from core.orc import orc
from core.screenshot import capture_screen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r'.\utils\chromedriver.exe')
browser.get('https://www.google.com')

while True:

    go = input('输入回车继续运行,输入 n 回车结束运行: ')
    if go == 'n':
        break

    capture_screen()

    o = orc(app_id='10689024', api_key='ABTXXPeylq1B6cUp0CdDoxlP', secret_key='dnuV0MfxVI9xIZtewfdA3qutGTPAflzS')

    question, choices = o.get_result()
    keyword = question + ' '
    for str in choices:
        keyword = keyword + str + ' '

    print(keyword)
    elem = browser.find_element_by_id("lst-ib")
    elem.clear()
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)

    print('----------------------------------')