import ollama
import os
import pyautogui
import keyboard
from  datetime import datetime

model = "<insert model name>"
# Moondream recommended

try:
    os.mkdir("logs/")
except FileExistsError:
    print("Previous logs found.")

running = True
def describe():
    curr_time = datetime.now()
    curr_time = curr_time.strftime("%Y-%m-%d %H-%M-%S")
    screenshot_name = f"Image-{curr_time}.png"
    log_name = f"Log{curr_time}.png"
    pyautogui.screenshot().save("logs/"+screenshot_name)
keyboard.add_hotkey('ctrl+alt+l', describe)
keyboard.wait('esc')