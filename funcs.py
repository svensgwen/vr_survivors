import sys
import json
from utils import *

DATA_FILE = "data/data.json"
STORY_FILE = "story.json"
GAME_FILE = "data/data.json"
PLAYER_FILE = "saves/player.json"
COMPANION_FILE = "data/companion.json"
INVENTORY_FILE = "data/inventory.json"
RECIPES_FILE = "data/recipes.json"
USE_EFFECTS_FILE = "data/use_effects.json"

def load_game_data(GAME_FILE):
    try:
        with open(GAME_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ data.json not found.")
        sys.exit()

gameData = load_game_data(GAME_FILE)

inventory = load_json(INVENTORY_FILE)
recipes = load_json(RECIPES_FILE)
use_effects = load_json(USE_EFFECTS_FILE)

# Player Data Loading
playerData = load_json(PLAYER_FILE)
player = playerData["player"]
health = player["health"]
attack = player["attack"]
speed = player["speed"]

# # Companion Data Loading
# companionData = load_json(COMPANION_FILE)
# companion = companionData["companion"]
# c_name = companion["name"]
# c_health = companion["health"]
# c_energy = companion["attack"]
# c_hunger = companion["speed"]
# c_inventory = companion["inventory"]

def craft_item(item_name, recipes, inventory):
    if item_name not in recipes:
        return False, "Item doesn't exist in recipes."
    required = recipes[item_name]

    # Check if inventory has all required items in enough quantity
    for item, amount in required.items():
        if inventory.get(item, 0) < amount:
            return False, f"Not enough {item} to craft {item_name}."

    # Deduct items from inventory
    for item, amount in required.items():
        inventory[item] -= amount

    # Add the crafted item to inventory
    add_item(item_name, 1, inventory)

    return True, f"{item_name} successfully crafted."

# # Example Usage
# success, message = craft_item("wooden_sword", recipes, inventory)


def add_item(item_name, amount, inventory):
    if amount <= 0:
        return False, "Amount must be positive."

    inventory[item_name] = inventory.get(item_name, 0) + amount
    return True, f"Added {amount}x {item_name}."

# # Example Usage
# print(add_item("potion", 3, inventory))   # Add potions
# print(add_item("stone", 5, inventory))    # Add stones



def delete_item(item_name, inventory):
    if item_name in inventory:
        del inventory[item_name]
        return True, f"{item_name} deleted from inventory."
    return False, f"{item_name} not found in inventory."



def use_item(item_name, inventory, use_effects=None):
    if inventory.get(item_name, 0) <= 0:
        return False, f"You don't have any {item_name} to use."

    # Reduce item count
    inventory[item_name] -= 1
    if inventory[item_name] == 0:
        del inventory[item_name]

    # Optional effects
    if use_effects and item_name in use_effects:
        for effect_item, effect_amount in use_effects[item_name].items():
            inventory[effect_item] = inventory.get(effect_item, 0) + effect_amount
        return True, f"Used {item_name}. Effect applied."

    return True, f"Used {item_name}. No special effect."

# # Example Usage
# print(use_item("potion", inventory, use_effects))  # Should use 1 potion and add 1 empty bottle

def clean_inventory(inventory):
    removed_items = [item for item, amount in inventory.items() if amount <= 0]
    for item in removed_items:
        del inventory[item]
    return removed_items

# # Example Usage
# removed = clean_inventory(inventory)
# print("Removed items:", removed)
# print("Cleaned inventory:", inventory)


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
