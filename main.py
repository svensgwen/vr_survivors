
# ==================================================================================================================
#                                                   PYTHON IMPORTS                                                  |
# ==================================================================================================================
import sys

# ==================================================================================================================
#                                                   EXTERNAL IMPORTS                                                |
# ==================================================================================================================

from rich.console import Console

console = Console()

# ==================================================================================================================
#                                                   CUSTOM IMPORTS                                                  |
# ==================================================================================================================
from funcs import *

# ==================================================================================================================
#                                                   MAIN MENU                                                       |
# ==================================================================================================================

def continue_game():
    clear_screen()
    game_menu()

def load_game():
    clear_screen()
    print("=================== 📂 Loading Game ===================")

def new_game():
    clear_screen()
    print("=================== 🌅 Initializing New Game ===================")

def options_menu():
    clear_screen()
    print("=================== ⚙️  Options ===================")
    print("1. Image Gallery")
    print("2. Recipies Gallery")
    print("0. Menu")

def hackit():
    clear_screen()
    print("=================== 💻  Dev mode ===================")
    print("1. Add Item to Inventory")
    print("0. Menu")

    choice = input("Your choice: ")

    match choice:

        # Add Item Function
        case '1':
            item = input("Enter item name to add: ")
            try:
                amount = int(input("Enter amount: "))
                success, msg = add_item(item, amount, inventory)
                print(msg)
            except ValueError:
                print("Amount must be a number.")

        case '0':
            clear_screen()
            main_menu()

def exit_game():
    clear_screen()
    print("=================== Exiting.. Stay Alive... 👋 ===================")
    sys.exit()

def main_menu():
    clear_screen()
    print("=================== MAIN MENU 📖 ===================")
    print("1. Continue")
    print("2. Load Game")
    print("3. New Game")
    print("4. Options")
    print("5. HackIt")
    print("0. Exit")
    
    choice = input("Select an option: ")

    match choice:

        case '1':
            continue_game()
        
        case '2':
            load_game()
        
        case '3':
            new_game()
        
        case '4':
            options_menu()
        
        case '5':
            hackit()
        
        case '0':
            exit_game()
        
        case _:
            print("⚠️ Invalid input. Try again.")

# ==================================================================================================================
#                                                   GAME MENU
# ==================================================================================================================

# ---------------------------------------------- SCAVENGE MENU -----------------------------------------------------
def scavenge():
    clear_screen()
    print("\n")
    print("=================== 🔍 Scavenge ===================")

# ---------------------------------------------- INVENTORY MENU -----------------------------------------------------
def display_inventory(inventory):
    clear_screen()
    print("\n")
    print("=================== INVENTORY 🧺 ===================")
    if not inventory:
        print("  (empty)")
    else:
        for i, (item, count) in enumerate(inventory.items(), 1):
            print(f"  {i}. {item} x{count}")
    print("Choose an action:")
    print("1. Use Item")
    print("2. Craft Item")
    print("3. Drop Item")
    print("0. Menu")

    choice = input("Your choice: ")

    match choice:

        # Use Item Function
        case '1':
            items = list(inventory.keys())
            if not items:
                print("Nothing to use.")
            for i, item in enumerate(items, 1):
                print(f"  {i}. {item}")
            try:
                item_index = int(input("Enter number of item to use: ")) - 1
                item_name = items[item_index]
                success, msg = use_item(item_name, inventory, use_effects)
                print(msg)
            except (ValueError, IndexError):
                print("Invalid selection.")
            clean_inventory(inventory)

        # Craft Item Function
        case '2':
            display_recipes(recipes)
            try:
                item_index = int(input("Enter number of item to craft: ")) - 1
                item_name = list(recipes.keys())[item_index]
                success, msg = craft_item(item_name, recipes, inventory)
                print(msg)
            except (ValueError, IndexError):
                print("Invalid selection.")
            clean_inventory(inventory)

        case '3':
            item = input("Enter item name to drop: ")
            success, msg = delete_item(item, inventory)
            print(msg)

        case _: print("⚠️ Invalid input. Try again.")

def display_recipes(recipes):
    print("\n")
    print("=================== CRAFTABLE ITEMS 🛠️ ===================")
    for i, (item, ingredients) in enumerate(recipes.items(), 1):
        reqs = ', '.join(f"{k}x{v}" for k, v in ingredients.items())
        print(f" {i}. {item} [{reqs}]")
    print()

def crafting_menu():
    clear_screen()
    display_recipes(recipes)
    print("=================== CRAFT ITEMS 🧤 ===================")
    try:
        item_index = int(input("Enter number of item to craft: ")) - 1
        item_name = list(recipes.keys())[item_index]
        success, msg = craft_item(item_name, recipes, inventory)
        print(msg)
    except (ValueError, IndexError):
        print("Invalid selection.")
    clean_inventory(inventory)
# ------------------------------------------------- TRAVEL MENU -------------------------------------------------------

def travel():
    print("\n")
    print("=================== TRAVEL 🌅 ===================")

# ---------------------------------------------- PLAYER INFO MENU -----------------------------------------------------

# Function to display player info
def show_player_info():
    clear_screen()
    print("=================== PLAYER INFORMATION 🛈 ===================")
    print(f"Player Name: {player['name']} | Health: {player['health']} | Attack: {player['attack']} | Speed: {player['speed']} | Money: ${player['money']}")

def show_companion_info():
    clear_screen()
    print("=================== COMPANION INFORMATION 🛈 ===================")
    # print(f"Name: {companion['name']} | Health: {companion['health']} | Attack: {companion['attack']} | Speed: {companion['speed']} | Money: ${companion['money']}")

# -------------------------------------------------- HELP MENU --------------------------------------------------------

def help_menu():
    clear_screen()
    print("====================== Need Help ❓ ======================")
    print("1. Tips")
    print("2. Story")
    print("3. Characters")
    print("4. Creator Info")

def story_menu():
    display_story()

def game_menu():
    global inventory, recipes
    while True:
        print("\n")
        console.print("🧬 [bold cyan] ========== V R SURVIVORS ========== [/bold cyan] 🧬 ")
        console.print("[bold red]-------------------------------------------------------------[/bold red]")
        console.print(f"[bold magenta]Name: {player['name']}[/bold magenta] | [bold green]Health: {player['health']}[/bold green] | [bold]Money: ${player['money']}[/bold]")
        console.print("[bold red]-------------------------------------------------------------[/bold red]")
        console.print("1. 🔍 \t Scavenge")
        console.print("2. 🧰 \t Open Inventory")
        console.print("3. 🛠️ \t Craft Item")
        console.print("4. 🌅 \t Travel")
        console.print("5. 🧱 \t Build")
        console.print("6. 🛖 \t  Shelter")
        console.print("7. 📜 \t Recipies")
        console.print("8. 🏪 \t Store")
        console.print("9. '🛈' \t Player Info")
        console.print("10. ❓ \t Help")
        console.print("0. ❌ \t Exit")
        console.print("(ENTER). ↩️ \t MAIN MENU")
        choice = input("Select an option: ")
        
        match choice:
            
            # Scavenger Menu
            case '1':
                scavenge()

            # Open Inventory
            case '2': 
                display_inventory(inventory)

            # Craft Item
            case '3': 
                crafting_menu()
            
            # Travel
            case '4':
                clear_screen()

            # Build
            case '5':
                clear_screen()

            case '6':
                clear_screen()

            # Recipies
            case '7':
                clear_screen()
                display_recipes(recipes)

            # Player Information
            case '8': 
                clear_screen()
                show_player_info()
                # show_companion_info()

            # Help Menu
            case '9':
                help_menu()
            
            case '':
                main_menu()

            # Return to Main Menu
            case '0': 
                clear_screen()
                exit_game()
            
            case _: print(" ⚠️ Invalid input. Try again.")

if __name__ == "__main__":
    main_menu()
