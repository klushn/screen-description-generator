from ollama import chat
from ollama import ChatResponse
import os
import pyautogui
import keyboard
from  datetime import datetime

model = "<insert model name>"
# Moondream recommended for efficiency

system_prompt = """
You are a screen describer, you will briefly yet accurately describe what is on screen without using any extraneous words.
"""
prompt = "Describe: "

try:
    os.mkdir("logs/")
except FileExistsError:
    print("Previous logs found.")

def describe():
    messages = [{
        'role': 'system',
        'content': system_prompt,
    },]
    curr_time = datetime.now()
    curr_time = curr_time.strftime("%Y-%m-%d %H-%M-%S")
    screenshot_name = f"Image-{curr_time}.png"
    log_name = f"Log{curr_time}.txt"
    pyautogui.screenshot().save("logs/"+screenshot_name)
    messages.append({"role": "user", "content": prompt, "images":["logs/"+screenshot_name]})
    print("Saved Screenshot.")
    response: ChatResponse = chat(model=model, messages=messages,)
    description = response.message.content
    print("Created description.")

    with open("logs/"+log_name, "w+") as f:
        f.write(description)
keyboard.add_hotkey('ctrl+alt+l', describe)
keyboard.wait('esc')
