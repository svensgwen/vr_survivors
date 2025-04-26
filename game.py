# =================================================================================================================
#                                                   PYTHON IMPORTS                                                 |
# =================================================================================================================
import os
import json
import random

# ==================================================================================================================
#                                                   EXTERNAL IMPORTS                                                |
# ==================================================================================================================

from rich.console import Console

console = Console()


# =================================================================================================================
#                                                       UTILS                                                      |
# =================================================================================================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")

def seperator():
    print("xX--------------------xX")

# =================================================================================================================
#                                                       VALUES                                                      |
# =================================================================================================================


# ---------------------------------------------------- CONSTANTS ---------------------------------------------------
# MAX VALUES
HPMAX = 6000
ATKMAX = 600

# ________________ MAP ________________

MAP = [
        # x = 0          x = 1       x = 2       x = 3       x = 4      x =  5          x = 6
        ["plains",     "plains",   "plains",    "plains",   "forest", "mountain",       "cave"],    # y = 0
        ["forest",     "forest",   "forest",    "forest",   "forest",    "hills",   "mountain"],    # y = 1
        ["forest",     "fields",   "bridge",    "plains",    "hills",   "forest",      "hills"],    # y = 2
        ["plains",       "shop",     "town",     "mayor",   "plains",    "hills",   "mountain"],    # y = 3
        ["plains",     "fields",   "fields",    "plains",    "hills", "mountain",   "mountain"],    # y = 4
        ["forest",     "forest",    "plain",     "plain",    "hills",    "hills",      "hills"],    # y = 5
        ["mountain", "mountain",   "forest",    "forest",   "forest",    "plain",      "plain"]     # y = 6
]

Y_LEN = len(MAP)-1
X_LEN = len(MAP[0])-1

# ________________ CONTINENTS ________________

CONTINENTS = [""]

# ________________ BIOMES ________________
BIOMES = ["forest", "mountain", "highland", "savannah", "swamp"]

# ________________ LOCATIONS ________________

FORTS = [
            "fort_rowan", "garronfort", "valemont", "caelmoor", "thalwyn", "aurelith"
            "stormreach", "highvale", "cindrallis", "duskwatch", "wyrmholt", "crestfall",
            "elowen", "lunareth", "avenleigh"
        ]

TOWNS = ["brookmere", "clayrun", "driftmoor", "ravenstead", "redfey", "egglots", "meetfoy"]
# ________________ REGIONS ________________

FORESTS = ["thornveil", "elarwyn_woods", "milgrove", "visthorn_wild", "yll_fen", "windripple_fen"]

MOUNTAINS = ["drakspire_range", "karradun", "frostmourn_peaks", "ironhold_cliffs", "velkarth_divide", "snowrest"]

HIGHLANDS = ["caelwyn_reaches", "braemor", "stoneweld_rise", "galdran_moors", "eron_vale", "ashvar_plateau"]

SAVANNAHS = ["serathi_plains", "redhollow", "duskwind_expanse", "vaelor", "orrenreach", "kymi_flats"]

SWAMPS = ["stumprot", "murkwash", "wetlands", "madmarsh", "morvassa", "slithera"]

# ________________ ENEMIES ________________

ENEMIES = ["beast", "fallen", "rabble", "occult"]

BEASTS = [
    {"name": "wolf", "text": "🐺 Wolf"},
    {"name": "bear", "text": "🐻 Bear"},
    {"name": "fox", "text": "🦊 Fox"},
    {"name": "boar", "text": "🐗 Boar"},
    {"name": "panther", "text": "🐆 Panther"},
    {"name": "dragon", "text": "🐉 Dragon"}
]

FALLENS = [
    {"name": "fiend", "text": "😈 Fiend"},
    {"name": "ghost", "text": "👻 Ghost"},
    {"name": "ghoul", "text": "🧟 Ghoul"},
    {"name": "undead", "text": "💀 Undead"}
]



RABBLES = [
    {"name": "goblin", "text": "👺 Goblin"},
    {"name": "orc", "text": "👹 Orc"},
    {"name": "slime", "text": "🔵 Slime"}
]


OCCULTS = [
    {"name": "skull_dweller", "text": "☠️ Skull Dweller"},
    {"name": "giant", "text": "🦣 Giant"}
]


# ________________ ROLES ________________

ROLES = [
  {"name": "wizard", "text": "🧙 Wizard"},
  {"name": "knight", "text": "🛡️ Knight"},
  {"name": "archer", "text": "🏹 Archer"},
  {"name": "rogue", "text": "🗡️ Rogue"},
  {"name": "healer", "text": "💉 Healer"},
  {"name": "druid", "text": "🌿 Druid"},
  {"name": "barbarian", "text": "🪓 Barbarian"},
  {"name": "warlock", "text": "🔮 Warlock"},
  {"name": "adventurer", "text": "🧝 Adventurer"},
  {"name": "merchant", "text": "💰 Merchant"},
  {"name": "alchemist", "text": "⚗️ Alchemist"},
  {"name": "necromancer", "text": "☠️ Necromancer"},
  {"name": "bard", "text": "🎶 Bard"}
]


# ________________ POTIONS ________________

ITEMS = {
    "dragonsblood":{
        "cost": 95
    },
    "elixir":{
        "cost": 70
    },
    "bloodroot":{
        "cost": 55
    },
    "lumenvail":{
        "cost": 63
    },
    "mightonic":{
        "cost": 72
    },
    "ironbark":{
        "cost": 57
    },
    "shadowvail":{
        "cost": 36
    },
    "ashenvail":{
        "cost": 33
    },
    "phantomvail":{
        "cost": 82
    },
    "clarissence":{
        "cost": 72
    },
    "serpentoison":{
        "cost": 40
    },
    "snowdrops":{
        "cost": 67
    },
    "goldenleafvail":{
        "cost": 53
    }
}


# ________________ MOB STATS ________________

MOBS = {
    "goblin": {
        "hp": 375,
        "atk": 27,
        "exp": 22,
        "gold": 31
    },
    "orc": {
        "hp": 455,
        "atk": 55,
        "exp": 37,
        "gold": 25
    },
    "slime": {
        "hp": 200,
        "atk": 32,
        "exp": 7,
        "gold": 15
    },
    "dragon":{
        "hp": 999,
        "atk": 62,
        "gold": 6799
    }
} 


# --------------------------------------------------- VARIABLES ----------------------------------------------------
hp = 100
atk = 10

# ---------------------------------------------------- VARIABLES ---------------------------------------------------

travel = False

run = True
play = False
rules = False
key = False
fight = False
buy = False
speak = False
boss = False
gold = 0
x = 0
y = 0
name = "player"
inventory = {}


# =================================================================================================================
#                                                       FUNCTIONS                                                  |
# =================================================================================================================


def probability(int):
    if random.randint(0, 100) < int:
        return True
    else:
        return False

def rarity(int):
    rareness = int * 10
    chance = 100 - rareness
    return probability(chance)

def get_input():
    value = input("O.o |: ")
    
    # Check if the input is a valid number
    if value.isdigit():
        return value # Return the value
    else:
        raise ValueError("Input must be a number!")  # Raise error if not a number


# ---------------------------------------------------- GAME DATA ---------------------------------------------------

game_data = {
    "name": name,
    "hp": hp,
    "atk": atk,
    "gold": gold,
    "inventoty": inventory,
    "x": x,
    "y": y
}

def save_game_data(game_data):
    with open("save.dat", "w") as file:
        json.dump(game_data, file, indent=4)

def load_game_data():
    with open("save.dat", "r") as file:
        game_data = json.load(file)
    return game_data

# ----------------------------------------------- INVENTORY FUNCTIONS ---------------------------------------------
def add_item(game_data, item_name, amount=1):
    inventory = game_data["inventory"]
    if item_name in inventory:
        inventory[item_name] += amount
    else:
        inventory[item_name] = amount

def remove_item(game_data, item_name, amount=1):
    inventory = game_data["inventory"]
    if item_name in inventory:
        inventory[item_name] -= amount
        if inventory[item_name] <= 0:
            del inventory[item_name]
    else:
        print(f"{item_name} not in inventory, can't remove.")


# ------------------------------------------------- ACTION FUNCTIONS ---------------------------------------------

def heal(amount):
    global hp
    if hp + amount < HPMAX:
        hp += amount
    else:
        hp = HPMAX
    return hp

def use_potion(potion):
    if potion == "health_potion":
        heal(50)
    elif potion == "elixir":
        heal(500)

# ------------------------------------------------ MOVEMENT FUNCTIONS ---------------------------------------------

def travel(dir):
    match dir:

        # North
        case '1':
            if y > 0:
                y -= 1

        # East
        case '2':
            if x < X_LEN:
                x += 1

        # South
        case '3':
            if y < Y_LEN:
                y += 1

        # West
        case '4':
            if x > 0:
                x -= 1

# ------------------------------------------------- ATTACK FUNCTIONS ----------------------------------------------

def get_enemy_stats(enemy):
    enemy_stats = {
        {
            "enemy_hpmax": MOBS[enemy]["hp"],
            "enemy_hp": MOBS[enemy]["hp"],
            "enemy_atk": MOBS[enemy]["atk"],
            "enemy_gold": MOBS[enemy]["gold"]
        }
    }
    return enemy_stats

def attack_enemy(enemy, atk):
    enemy_stats = get_enemy_stats()
    enemy_hp = enemy_stats["hp"]
    enemy_hp -= atk
    if enemy_hp > 0:
                return True, enemy, enemy_hp
    else: 
        loot_enemy(enemy)
        return False, enemy
    
def loot_enemy(enemy):
    enemy_stats = get_enemy_stats(enemy)
    gold += enemy_stats["gold"]
    
def fight(enemy):
    attack_enemy(enemy)

# ------------------------------------------------- SHOP FUNCTIONS -----------------------------------------------

def buy_item(item):
    pass

def upgrade_weapon():
    pass

def buy_potion(potion):
    pass


# ---------------------------------------------------- EQUIP FUNCTIONS ----------------------------------------------

def wear():
    pass

def strip():
    pass



# =================================================================================================================
#                                         ************* GUI *************                                          |
# =================================================================================================================

def main_menu():
    print("1. NEW GAME")
    print("2. LOAD GAME")
    print("3. DEV MODE")
    print("4. SAVE & QUIT GAME")

    choice = get_input()
    match choice:
        case '1':
            new_game()
        case '2':
            pass
        case '3':
            pass
        case '4':
            save_game_data()
            quit()

def new_game():
    clear_screen()
    name = input("# What's your name, adventurer? |:")
    game_data["name"] = name
    save_game_data(game_data)



def game_menu():
    console.print("🧬 [bold cyan] ========== V R SURVIVORS ========== [/bold cyan] 🧬 ")
    console.print("[bold red]-------------------------------------------------------------[/bold red]")
    console.print(f"[bold magenta]Name: {name}[/bold magenta] | [bold green]Health: {hp}[/bold green] | [bold white]Money: ${gold}[/bold white]")
    console.print("[bold red]-------------------------------------------------------------[/bold red]")
    console.print("")
    console.print("1.  🔍 \t Scavenge ")
    console.print("2.  🧰 \t Open Inventory")
    console.print("3.  🏞️ \t Travel")
    console.print("4.  🏡 \t Home")
    console.print("5.  ⚙️ \t More Options")
    console.print("0.  ❌ \t Save & Exit")
    console.print("[⏎ Enter].   MAIN MENU")
    choice = get_input()
    match choice:
        case '1':
            pass
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
game_menu()

