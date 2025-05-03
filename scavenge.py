import random

# Regional loot tables by town
towns = {
    "Ebonreach": {
        "Common": ["Torn Robe", "Broken Wand", "Dusty Scroll"],
        "Uncommon": ["Mage's Ring", "Shadow Ink", "Obsidian Charm"],
        "Rare": ["Spellbook Fragment", "Ghostly Pendant"],
        "Epic": ["Ebon Flame Core", "Cursed Grimoire"],
        "Legendary": ["Voidheart Scepter"]
    },
    "Ironhold": {
        "Common": ["Rusty Axe", "Chipped Helmet", "Broken Pickaxe"],
        "Uncommon": ["Iron Gauntlets", "Forge Hammer"],
        "Rare": ["Molten Shield", "Fireproof Cloak"],
        "Epic": ["Core of the Mountain", "Titan's Anvil"],
        "Legendary": ["Heart of the Forge"]
    },
    "Sylvanhollow": {
        "Common": ["Twig Bow", "Deer Hide", "Acorn Amulet"],
        "Uncommon": ["Forest Charm", "Elf-made Boots"],
        "Rare": ["Moonlit Leaf Blade", "Spirit Antler Helm"],
        "Epic": ["Sylvan Staff", "Dryad's Whisper"],
        "Legendary": ["Crown of the Wilds"]
    }
}

# Drop chances
drop_chances = {
    "Common": 0.5,
    "Uncommon": 0.35,
    "Rare": 0.3,
    "Epic": 0.03,
    "Legendary": 0.02,
    "Mythic": 0.01
}

def scavenge(town, num_items=5):
    if town not in towns:
        print(f"❌ Town '{town}' not found. Known towns: {', '.join(towns.keys())}")
        return []

    loot_table = towns[town]
    print(f"\n🌆 Scavenging in {town}...\n")
    found_items = []

    for _ in range(num_items):
        roll = random.random()
        cumulative = 0
        for rarity, chance in drop_chances.items():
            cumulative += chance
            if roll <= cumulative:
                items = loot_table.get(rarity, [])
                if items:
                    item = random.choice(items)
                    found_items.append((item, rarity))
                break

    print("🎒 Loot Found:")
    for item, rarity in found_items:
        print(f" - {item} [{rarity}]")
    return found_items

# Main
if __name__ == "__main__":
    print("🏘️ Available Towns:", ', '.join(towns.keys()))
    town = input("🏞️ Enter the name of the town to scavenge: ")
    scavenge(town.strip())
