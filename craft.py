from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel

console = Console()

# ==================================================================================================================
#                                                   CUSTOM IMPORTS                                                  |
# ==================================================================================================================

from utils import *

# ---------------------------------------------------- JSON IMPORTS ----------------------------------------------------
INVENTORY_FILE = "data/inventory.json"

RECIPES_FILE = "data/recipes.json"
recipes = load_json(RECIPES_FILE)

# ---------------------------------------------------- FUNCTIONS ----------------------------------------------------

def load_inventory():
    inventory = load_json(INVENTORY_FILE)
    return inventory

'''
--- #####*** ADD ITEM ***##### ---
# Example Usage
print(add_item("Potion", 3, inventory))   # Add potions
print(add_item("Stone", 5, inventory))    # Add stones
print(inventory)
'''
def add_item(item_name, amount, inventory):
    if amount <= 0:
        return False, "Amount must be positive."
    inventory[item_name] = inventory.get(item_name, 0) + amount

def save_inventory(data):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(data, file)

def show_inventory():
    table = Table(title="Inventory", show_lines=True)
    table.add_column("Item", style="cyan")
    table.add_column("Quantity", style="magenta")
    inventory = load_inventory()
    for item, qty in inventory.items():
        table.add_row(item, str(qty))
    console.print(table)

def show_recipes():
    table = Table(title="Crafting Recipes", show_lines=True)
    table.add_column("ID", style="bold green")
    table.add_column("Item", style="bold yellow")
    table.add_column("Ingredients", style="white")
    
    craftable_items = []
    i = 1

    for item, ingredients in recipes.items():
        ingredients_str = ", ".join(f"{k} x{v}" for k, v in ingredients.items())
        if can_craft(item):
            table.add_row(str(i), item, ingredients_str)
            craftable_items.append(item)
            i += 1
        else:
            table.add_row("-", f"[grey]{item}[/grey]", f"[grey]{ingredients_str}[/grey]")

    console.print(table)
    return craftable_items


def can_craft(item):
    required = recipes[item]
    inventory = load_inventory()
    return all(inventory.get(k, 0) >= v for k, v in required.items())

def craft(item):
    required = recipes[item]
    if can_craft(item):
        for k, v in required.items():
            inventory = load_inventory()
            inventory[k] -= v
        console.print(f"[bold green]Successfully crafted {item}![/bold green]")
        add_item(item, 1, inventory)
        save_inventory(inventory)
        show_inventory()
    else:
        console.print(f"[bold red]Not enough resources to craft {item}.[/bold red]")
        missing_table = Table(title=f"Required Materials for {item}", show_lines=True)
        missing_table.add_column("Item", style="cyan")
        missing_table.add_column("Required", style="magenta")
        missing_table.add_column("You Have", style="yellow")
        
        for k, v in required.items():
            have = inventory.get(k, 0)
            missing_table.add_row(k, str(v), str(have))
        
        console.print(missing_table)
        pause()


def main_menu():
    while True:
        console.print(Panel("⚒️  [bold cyan]Crafting Menu[/bold cyan] ⚒️", expand=False))
        craftable_items = show_recipes()
        
        if not craftable_items:
            console.print("[bold red]You don't have resources to craft anything.[/bold red]")
            pause()
            continue

        choice = IntPrompt.ask("Enter the recipe ID to craft (0 to exit)", default=0)

        if choice == 0:
            console.print("[bold yellow]Goodbye![/bold yellow]")
            break

        if 1 <= choice <= len(craftable_items):
            craft(craftable_items[choice - 1])
        else:
            console.print("[bold red]Invalid choice.[/bold red]")

        pause()


if __name__ == "__main__":
    main_menu()
