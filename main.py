import pyautogui
import time
import subprocess

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

subprocess.Popen(["firefox"])
time.sleep(1)

pyautogui.click(x=1207, y=405)
pyautogui.write("franciellysantos876@gmail.com")

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# email Point(x=1207, y=405)

# senha Pointx=902, y=537