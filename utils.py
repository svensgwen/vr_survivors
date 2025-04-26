import os
import time
import json
import random
import subprocess
from alive_progress import alive_bar

# Clears screen based on OS
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")

# Pause before clearing the screen
def pause():
    input("\nPress Enter to continue...")

def rand_int(INT=10):
    return random.randint(1, INT)

def progress(SLEEP=0.05):
    with alive_bar(100) as bar:
        for i in range(100):
            time.sleep(SLEEP)
            bar()

def open_image(IMAGE_PATH):
    subprocess.run(["xdg-open", IMAGE_PATH])

def seperator():
    print("xX--_________________----------------------___________________ --Xx")

# =========================
#       JSON Handlers
# =========================
def load_json(path):
    with open(path, "r") as f:
        return json.load(f)
    
def save_json(data, filename, indent):
    with open(filename, "w") as file:
        json.dump(data, file, indent)

def get_json_keys(data):
    key_list = list(data.keys())
    return key_list
