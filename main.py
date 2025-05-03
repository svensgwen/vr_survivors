
# ==================================================================================================================
#                                                   PYTHON IMPORTS                                                  |
# ==================================================================================================================

import os
import random

# ==================================================================================================================
#                                                   EXTERNAL IMPORTS                                                |
# ==================================================================================================================

from rich.console import Console

console = Console()

# ==================================================================================================================
#                                                   CUSTOM IMPORTS                                                  |
# ==================================================================================================================

from utils import clear_screen, seperator

# ---------------------------------------------------- CONSTANTS ----------------------------------------------------

HPMAX = 6000
ATKMAX = 600

TIMEFORMAT = ["simple", "advanced"]

# NOTE - World Map shows continents
WORLD_MAP = [
         #     x = 0                          x = 1                x = 2
         ["norvallis",           "duskwind expanse",          "orynthia"],           # y = 0
         ["auralen",                 "galwyn wilds",         "cindrosia"],           # y = 1
         ["rongrove",                   "blackmere",         "slytheria"]            # y = 2
]

GALWYN = [
        # 
        [""], # y = 0
        [    "pen gent",     "pen garn",        "pen uchaf",       "bryn gorge",         "mavar gorge",      "pen kerrig"], # y = 1
        [      "yenfey",     "eronvale",         "nytheris",       "fort rowen",        "cairn camain",    "cairin fidar"], # y = 2
        [ "cairin gorm", "cairin cloch",  "cairin glascore",       "cairn darg",          "creag dhor",      "creag garr"], # y = 3
        [  "creag morr", "creag meagir",     "",  "sterling"], # y = 4
        []  # y = 5
]

MAP = [
         #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
        ["plains",   "plains",   "plains",   "plains",   "forest",  "mountain",        "cave"],     # y = 0
        ["forest",   "forest",   "forest",   "forest",   "forest",     "hills",    "mountain"],     # y = 1
        ["forest",   "fields",   "bridge",   "plains",    "hills",    "forest",       "hills"],     # y = 2
        ["plains",     "shop",     "town",    "mayor",   "plains",     "hills",    "mountain"],     # y = 3
        ["plains",   "fields",   "fields",   "plains",    "hills",  "mountain",    "mountain"],     # y = 4
        ["forest",   "plains",   "plains",   "plains",    "forest", "mountain",    "mountain"],     # y = 5
        ["fields",   "fields",   "fields",   "plains",    "hills",     "hills",       "hills"]      # y = 6
    ]
Y_LEN = len(MAP)-1
X_LEN = len(MAP[0])-1

# ---------------------------------------------------- VARIABLES ----------------------------------------------------

player = {
    "name": "galgor",
    "health": 100,
    "money": 1000000,
    "current_location": "fort rowen"
}

def main_menu():
    game_menu()


def continue_game():
    clear_screen()
    game_menu()

def game_menu():
        print("\n")
        console.print("🧬 [bold cyan] ========== V R SURVIVORS ========== [/bold cyan] 🧬 ")
        console.print("[bold red]-------------------------------------------------------------[/bold red]")
        console.print(f"[bold magenta]Name: {player['name']}[/bold magenta] \t [bold]|[/bold] [bold green]Health: {player['health']}[/bold green]  \t [bold]|[/bold] [bold]Money: [/bold][bold green]${player['money']}[/bold green]")
        console.print("[bold red]-------------------------------------------------------------[/bold red]")
        console.print(f"\t \t [bold cyan]LOCATION: {player['current_location']}[/bold cyan]")
        console.print("[bold green]-------------------------------------------------------------[/bold green]")
        console.print("1. 🔍 \t Scavenge")
        console.print("2. 🏹 \t Hunt")
        console.print("3. 🧰 \t Open Inventory")
        console.print("4. 🛠️ \t Craft Item")
        console.print("5. 🌅 \t Travel")
        console.print("6. 🧱 \t Build")
        console.print("7. 🛖 \t  Shelter")
        console.print("8. 📜 \t Recipies")
        console.print("9. 🏪 \t Store")
        console.print("10. [bold green]🛈[/bold green] \t Player Info")
        console.print("11. ❓ \t Help")
        console.print("0. ❌ \t Exit")
        console.print("(ENTER). ↩️ \t MAIN MENU")

if __name__ == "__main__":
    main_menu()