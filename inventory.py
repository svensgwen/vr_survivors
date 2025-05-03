def remove_item(item_name, inventory):
    if item_name in inventory:
        del inventory[item_name]
        return True, f"{item_name} removed from inventory."
    return False, f"{item_name} not found in inventory."



'''
--- #####*** CLEAN INVENTORY ***##### ---
# Example Usage
removed = clean_inventory(inventory)
print("Removed items:", removed)
print("Cleaned inventory:", inventory)
'''
def clean_inventory(inventory):
    removed_items = [item for item, amount in inventory.items() if amount <= 0]
    for item in removed_items:
        del inventory[item]
    return removed_items


