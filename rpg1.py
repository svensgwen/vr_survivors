import os
import random

# ========================================
#              GAME CONSTANTS
# ========================================
USER_DATA = "user.dat"
HPMAX = 6000
ATKMAX = 600

MAP = [
    ["plains", "plains", "plains", "plains", "forest", "mountain", "cave"],
    ["forest", "forest", "forest", "forest", "forest", "hills", "mountain"],
    ["forest", "fields", "bridge", "plains", "hills", "forest", "hills"],
    ["plains", "shop", "town", "mayor", "plains", "hills", "mountain"],
    ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain"],
    ["forest", "plains", "plains", "plains", "forest", "mountain", "mountain"],
    ["fields", "fields", "fields", "plains", "hills", "hills", "hills"]
]

Y_LEN = len(MAP) - 1
X_LEN = len(MAP[0]) - 1

BIOMES = {
    "plains":    {"text": "PLAINS",       "enemies": True},
    "forest":    {"text": "WOODS",        "enemies": True},
    "fields":    {"text": "FIELDS",       "enemies": False},
    "bridge":    {"text": "BRIDGE",       "enemies": True},
    "town":      {"text": "TOWN CENTRE",  "enemies": False},
    "shop":      {"text": "SHOP",         "enemies": False},
    "mayor":     {"text": "MAYOR",        "enemies": False},
    "cave":      {"text": "CAVE",         "enemies": False},
    "mountain":  {"text": "MOUNTAIN",     "enemies": True},
    "hills":     {"text": "HILLS",        "enemies": True}
}

MOBS = {
    "goblin": {"hp": 370, "atk": 30, "gold": 8},
    "orc":    {"hp": 480, "atk": 50, "gold": 18},
    "slime":  {"hp": 100, "atk": 20, "gold": 12},
    "dragon": {"hp": 999, "atk": 80, "gold": 600}
}

ENEMY_LIST = ["goblin", "orc", "slime"]

# ========================================
#              GAME STATE
# ========================================

game = {
    "name": "",
    "hp": 600,
    "atk": 35,
    "potion": 1,
    "elixir": 0,
    "gold": 0,
    "x": 0,
    "y": 0,
    "key": False
}

# Flags
flags = {
    "run": True,
    "menu": True,
    "play": False,
    "fight": False,
    "boss": False,
    "buy": False,
    "speak": False,
    "rules": False,
    "standing": True
}

# ========================================
#               UTILITIES
# ========================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def separator():
    print("xX-----------------------------------------------xX")

def save_game():
    with open(USER_DATA, "w") as f:
        for value in game.values():
            f.write(str(value) + "\n")

def load_game():
    try:
        with open("load.txt", "r") as f:
            data = f.read().strip().splitlines()
            keys = list(game.keys())
            for i in range(len(data)):
                if keys[i] == "key":
                    game[keys[i]] = data[i] == "True"
                elif keys[i] in ["hp", "atk", "potion", "elixir", "gold", "x", "y"]:
                    game[keys[i]] = int(data[i])
                else:
                    game[keys[i]] = data[i]
            return True
    except Exception:
        return False

def heal(amount):
    game["hp"] = min(game["hp"] + amount, HPMAX)
    print(f"{game['name']}'s HP refilled to {game['hp']}!")

# ========================================
#               BATTLE
# ========================================

def battle():
    enemy = "dragon" if flags["boss"] else random.choice(ENEMY_LIST)
    stats = MOBS[enemy]
    enemy_hp = stats["hp"]

    while flags["fight"]:
        clear_screen()
        separator()
        print(f"Defeat the {enemy.upper()}!")
        separator()
        print(f"{enemy.upper()} HP: {enemy_hp}/{stats['hp']}")
        print(f"{game['name']} HP: {game['hp']}/{HPMAX}")
        print(f"POTIONS: {game['potion']} | ELIXIRS: {game['elixir']}")
        separator()
        print("1 - ATTACK")
        if game["potion"] > 0: print("2 - USE POTION (30HP)")
        if game["elixir"] > 0: print("3 - USE ELIXIR (50HP)")
        separator()

        choice = input("# ")

        if choice == "1":
            enemy_hp -= game["atk"]
            print(f"You dealt {game['atk']} damage.")
            if enemy_hp > 0:
                game["hp"] -= stats["atk"]
                print(f"{enemy.upper()} dealt {stats['atk']} damage.")
            input("> ")

        elif choice == "2" and game["potion"] > 0:
            game["potion"] -= 1
            heal(30)
            game["hp"] -= stats["atk"]
            print(f"{enemy.upper()} dealt {stats['atk']} damage.")
            input("> ")

        elif choice == "3" and game["elixir"] > 0:
            game["elixir"] -= 1
            heal(50)
            game["hp"] -= stats["atk"]
            print(f"{enemy.upper()} dealt {stats['atk']} damage.")
            input("> ")

        if game["hp"] <= 0:
            print(f"{enemy.upper()} defeated {game['name']}... GAME OVER.")
            flags.update(run=False, play=False, fight=False)
            input("> ")
            return

        if enemy_hp <= 0:
            print(f"You defeated the {enemy.upper()}!")
            game["gold"] += stats["gold"]
            print(f"+{stats['gold']} GOLD")
            if random.randint(0, 100) < 30:
                game["potion"] += 1
                print("You found a potion!")
            if enemy == "dragon":
                print("You beat the game! Congrats.")
                flags.update(run=False, play=False, boss=False)
            flags["fight"] = False
            input("> ")

# ========================================
#             SHOP & MAYOR
# ========================================

def shop():
    while flags["buy"]:
        clear_screen()
        separator()
        print(f"Welcome to the Shop | GOLD: {game['gold']}")
        print(f"POTIONS: {game['potion']} | ELIXIRS: {game['elixir']} | ATK: {game['atk']}")
        separator()
        print("1 - Potion (5G) | 2 - Elixir (8G) | 3 - Upgrade (+2ATK, 10G) | 4 - Leave")
        separator()

        choice = input("# ")
        if choice == "1" and game["gold"] >= 5:
            game["gold"] -= 5
            game["potion"] += 1
        elif choice == "2" and game["gold"] >= 8:
            game["gold"] -= 8
            game["elixir"] += 1
        elif choice == "3" and game["gold"] >= 10:
            game["gold"] -= 10
            game["atk"] += 2
        elif choice == "4":
            flags["buy"] = False
        else:
            print("Not enough gold.")
        input("> ")

def mayor():
    clear_screen()
    print(f"Mayor: Hello, {game['name']}!")
    if game["atk"] < 10:
        print("You're not strong enough for the dragon.")
        game["key"] = False
    else:
        print("You seem ready. Take this key!")
        game["key"] = True
    input("> ")
    flags["speak"] = False

def cave():
    clear_screen()
    print("You stand before the dragon's cave.")
    if game["key"]:
        print("1 - Use Key | 2 - Leave")
        if input("# ") == "1":
            flags.update(boss=True, fight=True)
            battle()
    else:
        print("You need a key.")
        input("> ")
    flags["boss"] = False

# ========================================
#               MAIN LOOP
# ========================================

while flags["run"]:
    while flags["menu"]:
        clear_screen()
        print("1 - New Game\n2 - Load Game\n3 - Rules\n4 - Quit")
        choice = input("# ")

        if choice == "1":
            game["name"] = input("Name: ")
            flags.update(menu=False, play=True)
        elif choice == "2" and load_game():
            print(f"Welcome back, {game['name']}!")
            input("> ")
            flags.update(menu=False, play=True)
        elif choice == "3":
            print("Explore, fight, level up, defeat the dragon. Good luck.")
            input("> ")
        elif choice == "4":
            flags["run"] = False

    while flags["play"]:
        save_game()
        clear_screen()

        biome = MAP[game["y"]][game["x"]]
        if not flags["standing"] and BIOMES[biome]["enemies"] and random.randint(0, 100) < 30:
            flags["fight"] = True
            battle()

        separator()
        print(f"LOCATION: {BIOMES[biome]['text']}")
        print(f"NAME: {game['name']} | HP: {game['hp']} | ATK: {game['atk']} | GOLD: {game['gold']}")
        print(f"POS: ({game['x']}, {game['y']}) | POTIONS: {game['potion']} | ELIXIRS: {game['elixir']}")
        separator()
        print("0 - SAVE & QUIT | 1 - NORTH | 2 - EAST | 3 - SOUTH | 4 - WEST")
        print("5 - USE POTION | 6 - USE ELIXIR | 7 - ENTER LOCATION")
        separator()

        dest = input("# ")
        flags["standing"] = True

        if dest == "0":
            flags.update(play=False, menu=True)
            save_game()
        elif dest == "1" and game["y"] > 0:
            game["y"] -= 1
            flags["standing"] = False
        elif dest == "2" and game["x"] < X_LEN:
            game["x"] += 1
            flags["standing"] = False
        elif dest == "3" and game["y"] < Y_LEN:
            game["y"] += 1
            flags["standing"] = False
        elif dest == "4" and game["x"] > 0:
            game["x"] -= 1
            flags["standing"] = False
        elif dest == "5" and game["potion"] > 0:
            game["potion"] -= 1
            heal(30)
            input("> ")
        elif dest == "6" and game["elixir"] > 0:
            game["elixir"] -= 1
            heal(50)
            input("> ")
        elif dest == "7":
            if biome == "shop":
                flags["buy"] = True
                shop()
            elif biome == "mayor":
                flags["speak"] = True
                mayor()
            elif biome == "cave":
                cave()
