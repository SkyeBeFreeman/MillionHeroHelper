import os
import time
import ctypes
import win32gui
import win32con
from win32com import client
from PIL import Image, ImageGrab

class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_long), 
            ('top', ctypes.c_long), 
            ('right', ctypes.c_long), 
            ('bottom', ctypes.c_long)] 
    def __str__(self): 
        return str((self.left, self.top, self.right, self.bottom)) 


def process_image(directory='screenshots', filename='screenshot.png'):
    img = Image.open(os.path.join(directory, filename))

    # 问题
    img_question = img.crop((50, 300, 1000, 500))
    img_question.save(os.path.join(directory, 'screenshot_question.png'))

    # 选项A
    img_a = img.crop((100, 500, 800, 600))
    img_a.save(os.path.join(directory, 'screenshot_a.png'))    

    # 选项B
    img_b = img.crop((100, 650, 800, 750))
    img_b.save(os.path.join(directory, 'screenshot_b.png'))

    # 选项C
    img_c = img.crop((100, 800, 800, 900))
    img_c.save(os.path.join(directory, 'screenshot_c.png'))   


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

