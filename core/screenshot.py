import os
import time
import ctypes
import win32gui
import win32com.client
import win32con
from PIL import Image, ImageGrab

class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_long), 
            ('top', ctypes.c_long), 
            ('right', ctypes.c_long), 
            ('bottom', ctypes.c_long)] 
    def __str__(self): 
        return str((self.left, self.top, self.right, self.bottom)) 

def capture_screen(filename="screenshot.png", directory="screenshots"):
    window = win32gui.FindWindow(None, '夜神模拟器')
    win32gui.ShowWindow(window, win32con.SW_RESTORE)
    shell = win32com.client.Dispatch("WScript.Shell")
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

