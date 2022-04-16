import pyautogui
import psutil

import subprocess
import time
from datetime import datetime


SCREEN_SHOT_FOLDER = r"C:\screenshot"
SCREEN_SHOT_FOLDER = r"C:\Users\user\Downloads"
# APP_PATH = r'C:\Users\jchao1\Desktop\LVCap.exe'
APP_PATH = r'%windir%\system32\notepad.exe'

# 不知道 APP_NAME 可留空，執行程式後根據提示輸入。
# 執行期間請不要開啟關閉任何程式，避免程式誤判。
APP_NAME = "notepad.exe"


def destroyed(proc_name: str) -> None:
    for proc in psutil.process_iter():
        # print(proc.name())
        if proc.name() == proc_name:
            proc.kill()


def screen_shot():
    now = datetime.now()
    now = now.strftime(r"%Y-%m-%d,%H-%M-%S.%f")
    now = now[:-4]
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(SCREEN_SHOT_FOLDER + fr'\{now}.jpg')
    print('Screen capture')


if not APP_NAME:
    app = {
        p.pid: p.name() for p in psutil.process_iter(['pid', "name"])
    }

try:
    # 依照平台調整開啟app的方式
    proc = subprocess.Popen(
        ["start", "/max", APP_PATH],
        shell=True
    )
except Exception as e:
    print(f'Open app failed: {e}')
else:
    print("app is starting...")
    time.sleep(5)

    if not APP_NAME:
        print("Your app might be one of these name below:")
        for p in psutil.process_iter(['pid', "name"]):
            if p.pid not in app:
                print(f"\t{p.name()}")
    screen_shot()
    print('Done')
finally:
    # 依照app開啟後的名稱，結束app
    if APP_NAME:
        destroyed(APP_NAME)
