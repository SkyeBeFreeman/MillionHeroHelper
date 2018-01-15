import os
import time
import ctypes
import win32gui
import win32con
from win32com import client
from PIL import Image, ImageGrab
from time import strftime

class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_long), 
            ('top', ctypes.c_long), 
            ('right', ctypes.c_long), 
            ('bottom', ctypes.c_long)] 
    def __str__(self): 
        return str((self.left, self.top, self.right, self.bottom)) 


def process_image(directory='screenshots', filename='screenshot.png'):
    print(strftime("%Y-%m-%d %H:%M:%S") + " 开始处理图片", flush=True)
    img = Image.open(os.path.join(directory, filename))

    # 问题
    img_question = img.crop((50, 200, 1000, 400))
    img_question.save(os.path.join(directory, 'screenshot_question.png'))

    # 选项们
    img_choices = img.crop((100, 500, 800, 900))
    img_choices.save(os.path.join(directory, 'screenshot_choices.png'))

    print(strftime("%Y-%m-%d %H:%M:%S") + " 处理图片结束", flush=True)


def capture_screen(directory='screenshots', filename='screenshot.png'):
    window = win32gui.FindWindow(None, '夜神模拟器')
    win32gui.ShowWindow(window, win32con.SW_RESTORE)
    shell = client.Dispatch('WScript.Shell')
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)

    # 等待夜神模拟器移动到窗口最前端
    time.sleep(1)
    rect = RECT()
    ctypes.windll.user32.GetWindowRect(window,ctypes.byref(rect))

    # 这里的27为删除窗口上面的状态栏所做的调整，大小可根据自己的模拟器调整
    rangle = (rect.left,rect.top + 27,rect.right,rect.bottom)
    img = ImageGrab.grab(rangle)

    # 调整图片尺寸
    img = img.resize((1080, 1920), Image.ANTIALIAS)
    img.save(os.path.join(directory, filename))

    # 切分问题和选项
    process_image() 

