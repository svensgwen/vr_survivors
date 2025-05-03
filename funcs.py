import sys
import json
from utils import *

DATA_FILE = "data/data.json"
STORY_FILE = "story.json"
GAME_FILE = "data/data.json"
PLAYER_FILE = "saves/player.json"
COMPANION_FILE = "data/companion.json"
USE_EFFECTS_FILE = "data/use_effects.json"

def load_game_data(GAME_FILE):
    try:
        with open(GAME_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ data.json not found.")
        sys.exit()

gameData = load_game_data(GAME_FILE)
use_effects = load_json(USE_EFFECTS_FILE)

# Player Data Loading
playerData = load_json(PLAYER_FILE)
player = playerData["player"]
health = player["health"]
attack = player["attack"]
speed = player["speed"]

# ==================================================================================================================
#                                                   STORY FUNCTIONS                                                 |
# ==================================================================================================================

def load_story():
    data = load_json(DATA_FILE)
    if not data.get("story_shown", 0):
        story = load_json(STORY_FILE)
        chapters = story.get("chapters", {})
        display_story(chapters)
        data["story_shown"] = 1
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    else:
        print("\n Welcome Back... \n")

def display_story(chapters):
    print("\n🧬 THE BEGINNING OF V R SURVIVORS 🧬")
    for chapter_title, lines in chapters.items():
        input("\nNext chapter...(ENTER)\n")
        clear_screen()
        print(f"\n🔹 {chapter_title} 🔹\n")
        for line in lines:
            print(line)

# ==================================================================================================================
#                                                   NEW GAME FUNCTIONS                                              |
# ==================================================================================================================

def new_game():
    clear_screen()
    print("\n")
    create_player()

class Player:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

# Changed the file name where player data is stored
def update_player_file(filename):
    # Load existing JSON data
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    # Update the "load_player_file" key
    data["load_player_file"] = filename

    # Write the updated data back to the same file
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def create_player():
    print("\n")
    print("====== 👤 Creating New Player... ======")
    print("== ⚠️ NOTE: Use all lowercase letters, no symbols or numbers ==")
    fname = input("Enter Player First Name :")
    lname = input("Enter Player Second Name :")
    print(f"{fname}, {lname}")
    player = Player(fname, lname)
    player_data = {
        "name": player.fname,
        "lname": player.lname,
        "level": 1,
        "hp": 520,
        "inventory": {
            "canned_beans": 2,
            "water_pouch": 10
        }
    }
    filename = f"saves/{fname.lower()}_save.json"
    with open(filename, "w") as file:
        json.dump(player_data, file, indent=4)
    update_player_file(filename)

def choose_player():
    print("== Choose Player 👤 ==")

def choose_friends():
    print("== Choose Friends 👭 ==")
