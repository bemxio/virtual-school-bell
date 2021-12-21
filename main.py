from datetime import datetime
import configparser
import subprocess
import time

try:
    import keyboard
    is_pressed = keyboard.is_pressed
except ModuleNotFoundError:
    is_pressed = lambda key: False

def play(path):
    switches = ["-loglevel", "error", "-autoexit", "-nodisp"]
    subprocess.run(["ffplay", path] + switches)

# loading files
hours = configparser.ConfigParser()
hours.read("hours.ini")

# main stuff
print("Script loaded! Waiting for the next ring hour...")
while True:
    now = datetime.now().strftime("%H:%M")

    if now in hours:
        path = hours[now]["SoundPath"]

        print(f"It's {now}! Playing {path} now...\nWaiting for the next ring hour...")
        play(path)

    elif is_pressed(hours["Default"]["InvokeKey"]):
        path = hours["Default"]["SoundPath"]
        
        print(f"It's {now}! Playing {path} now...\nWaiting for the next ring hour...")
        play(path)
    
    time.sleep(1)
