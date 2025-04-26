# ==================================================================================================================
#                                                   PYTHON IMPORTS                                                  |
# ==================================================================================================================

import os
import random


# ==================================================================================================================
#                                                       UTILS                                                       |
# ==================================================================================================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def seperator():
    print("xX-----------------------------------------------xX")


# ---------------------------------------------------- CONSTANTS ----------------------------------------------------

HPMAX = 6000
ATKMAX = 600


# ---------------------------------------------------- VARIABLES ----------------------------------------------------

hp = 600
atk = 35

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False
potion = 1
elixir = 0
gold = 0
x = 0
y = 0


# -------------------------------------------------------- MAP --------------------------------------------------------

        
MAP = [
         #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
        ["plains",   "plains",   "plains",   "plains",   "forest",  "mountain",        "cave"],    # y = 0
        ["forest",   "forest",   "forest",   "forest",   "forest",     "hills",    "mountain"],    # y = 1
        ["forest",   "fields",   "bridge",   "plains",    "hills",    "forest",       "hills"],    # y = 2
        ["plains",     "shop",     "town",    "mayor",   "plains",     "hills",    "mountain"],    # y = 3
        ["plains",   "fields",   "fields",   "plains",    "hills",  "mountain",    "mountain"],    # y = 4
        ["forest",   "plains",   "plains",   "plains",    "forest", "mountain",    "mountain"],
        ["fields",   "fields",   "fields",   "plains",    "hills",     "hills",       "hills"]
    ]    

Y_LEN = len(MAP)-1
X_LEN = len(MAP[0])-1

biome = {
    "plains": {
        "text": "PLAINS",
        "enemies": True},
    "forest": {
        "text": "WOODS",
        "enemies": True},
    "fields": {
        "text": "FIELDS",
        "enemies": False},
    "bridge": {
        "text": "BRIGE",
        "enemies": True},
    "town": {
        "text": "TOWN CENTRE",
        "enemies": False},
    "shop": {
        "text": "SHOP",
        "enemies": False},
    "mayor": {
        "text": "MAYOR",
        "enemies": False},
    "cave": {
        "text": "CAVE",
        "enemies": False},
    "mountain": {
        "text": "MOUNTAIN",
        "enemies": True},
    "hills": {
        "text": "HILLS",
        "enemies": True,
    }
}

# ------------------------------------------------------ ENEMIES ------------------------------------------------------

e_list = ["goblin", "orc", "slime"]

mobs = {
    "goblin": {
        "hp": 370,
        "atk": 30,
        "gold": 8
    },
    "orc": {
        "hp": 480,
        "atk": 50,
        "gold": 18
    },
    "slime": {
        "hp": 100,
        "atk": 20,
        "gold": 12
    },
    "dragon": {
        "hp": 999,
        "atk": 80,
        "gold": 600
    }
}

def save():
    list = [
        name, str(hp), str(atk), str(potion), str(elixir), str(gold), str(x), str(y), str(key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()


def heal(amount):
    global hp
    if hp + amount < HPMAX:
        hp += amount
    else:
        hp = HPMAX
    print(name + "'s hp refilled to " + str(hp) + "!")


def battle():
    global fight, play, run, hp, potion, elixir, gold, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    enemy_hp = mobs[enemy]["hp"]
    enemy_hpmax = enemy_hp
    enemy_atk = mobs[enemy]["atk"]
    enemy_gold = mobs[enemy]["gold"]

    while fight:
        clear_screen()
        seperator()
        print("Defeat the " + enemy + "!")
        seperator()
        print(enemy + "'s hp: " + str(enemy_hp) + "/" + str(enemy_hpmax))
        print(name + "'s hp: " + str(hp) + "/" + str(HPMAX))
        print("POTIONS: " + str(potion))
        print("ELIXIR: " + str(elixir))
        seperator()
        print("1 - ATTACK")
        if potion > 0:
            print("2 - USE POTION (30HP)")
        if elixir > 0:
            print("3 - USE ELIXIR (50HP)")
        seperator()

        choice = input("# ")

        if choice == "1":
            enemy_hp -= atk
            print(name + " dealt " + str(atk) + " damage to the " + enemy + ".")
            if hp > 0:
                hp -= enemy_atk
                print(enemy + " dealt " + str(enemy_atk) + " damage to " + name + ".")
            input("> ")

        elif choice == "2":
            if potion > 0:
                potion -= 1
                heal(30)
                hp -= enemy_atk
                print(enemy + " dealt " + str(enemy_atk) + " damage to " + name + ".")
            else:
                print("No potions!")
            input("> ")

        elif choice == "3":
            if elixir > 0:
                elixir -= 1
                heal(50)
                hp -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No elixirs!")
            input("> ")

        if hp <= 0:
            print(enemy + " defeated " + name + "...")
            seperator()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            seperator()
            fight = False
            gold += enemy_gold
            print("You've found " + str(enemy_gold) + " gold!")
            if random.randint(0, 100) < 30:
                potion += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                seperator()
                print("Congratulations, you've finished the game!")
                boss = False
                play = False
                run = False
            input("> ")
            clear_screen()


def shop():
    global buy, gold, potion, elixir, atk

    while buy:
        clear_screen()
        seperator()
        print("Welcome to the shop!")
        seperator()
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(potion))
        print("ELIXIRS: " + str(elixir))
        print("atk: " + str(atk))
        seperator()
        print("1 - BUY POTION (30HP) - 5 GOLD")
        print("2 - BUY ELIXIR (MAXHP) - 8 GOLD")
        print("3 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
        print("4 - LEAVE")
        seperator()

        choice = input("# ")

        if choice == "1":
            if gold >= 5:
                potion += 1
                gold -= 5
                print("You've bought a potion!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if gold >= 8:
                elixir += 1
                gold -= 8
                print("You've bought an elixir!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if gold >= 10:
                atk += 2
                gold -= 10
                print("You've upgraded your weapon!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            buy = False


def mayor():
    global speak, key

    while speak:
        clear_screen()
        seperator()
        print("Hello there, " + name + "!")
        if atk < 10:
            print("You're not strong enough to face the dragon yet! Keep practicing and come back later!")
            key = False
        else:
            print("You might want to take on the dragon now! Take this key but be careful with the beast!")
            key = True

        seperator()
        print("1 - LEAVE")
        seperator()

        choice = input("# ")

        if choice == "1":
            speak = False


def cave():
    global boss, key, fight

    while boss:
        clear_screen()
        seperator()
        print("Here lies the cave of the dragon. What will you do?")
        seperator()
        if key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        seperator()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False

while run:
    while menu:
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")

        if rules:
            print("I'm the creator of this game and these are the rules.")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear_screen()
            name = input("# What's your name, adventurer? |:")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    hp = int(load_list[1][:-1])
                    atk = int(load_list[2][:-1])
                    potion = int(load_list[3][:-1])
                    elixir = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear_screen()
                    print("Welcome back, " + name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file!")
                    input("> ")
            except OSError:
                print("No loadable save file!")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  # autosave
        clear_screen()

        if not standing:
            if biome[MAP[y][x]]["enemies"]:
                if random.randint(0, 100) < 30:
                    fight = True
                    battle()

        if play:
            seperator()
            print("LOCATION: " + biome[MAP[y][x]]["text"])
            seperator()
            print("NAME: " + name)
            print("hp: " + str(hp) + "/" + str(HPMAX))
            print("atk: " + str(atk))
            print("POTIONS: " + str(potion))
            print("ELIXIRS: " + str(elixir))
            print("GOLD: " + str(gold))
            print("COORD:", x, y)
            seperator()
            print("0 - SAVE AND QUIT")
            if y > 0:
                print("1 - NORTH")
            if x < X_LEN:
                print("2 - EAST")
            if y < Y_LEN:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if potion > 0:
                print("5 - USE POTION (30HP)")
            if elixir > 0:
                print("6 - USE ELIXIR (50HP)")
            if MAP[y][x] == "shop" or MAP[y][x] == "mayor" or MAP[y][x] == "cave":
                print("7 - ENTER")
            seperator()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < X_LEN:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < Y_LEN:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if potion > 0:
                    potion -= 1
                    heal(30)
                else:
                    print("No potions!")
                input("> ")
                standing = True
            elif dest == "6":
                if elixir > 0:
                    elixir -= 1
                    heal(50)
                else:
                    print("No elixirs!")
                input("> ")
                standing = True
            elif dest == "7":
                if MAP[y][x] == "shop":
                    buy = True
                    shop()
                if MAP[y][x] == "mayor":
                    speak = True
                    mayor()
                if MAP[y][x] == "cave":
                    boss = True
                    cave()
            else:
                standing = True

