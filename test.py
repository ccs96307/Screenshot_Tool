# -*- coding: utf-8 -*-
import win32gui
import win32con
from PIL import ImageGrab

name = win32gui.GetWindowText(win32gui.WindowFromPoint((0, 0)))
print(name)

hwnd = win32gui.FindWindow(None, name)
if not hwnd:
    print('window not found!')
    exit()
else:
    print(hwnd)

# win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 強行顯示介面後才好截圖
# win32gui.SetForegroundWindow(hwnd)  # 將視窗提到最前
#  裁剪得到全圖
game_rect = win32gui.GetWindowRect(hwnd)
src_image = ImageGrab.grab(game_rect)
# src_image = ImageGrab.grab((game_rect[0] + 9, game_rect[1] + 190, game_rect[2] - 9, game_rect[1] + 190 + 450))
src_image.save('test.png')