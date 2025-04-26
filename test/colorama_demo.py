from colorama import init, Fore, Back, Style

init(autoreset=True)  # So each print resets colors

print("=== Foreground Colors ===")
print(Fore.BLACK   + "Black")
print(Fore.RED     + "Red")
print(Fore.GREEN   + "Green")
print(Fore.YELLOW  + "Yellow")
print(Fore.BLUE    + "Blue")
print(Fore.MAGENTA + "Magenta")
print(Fore.CYAN    + "Cyan")
print(Fore.WHITE   + "White")

print("\n=== Background Colors ===")
print(Back.BLACK   + "Black Background")
print(Back.RED     + "Red Background")
print(Back.GREEN   + "Green Background")
print(Back.YELLOW  + "Yellow Background")
print(Back.BLUE    + "Blue Background")
print(Back.MAGENTA + "Magenta Background")
print(Back.CYAN    + "Cyan Background")
print(Back.WHITE   + "White Background")

print("\n=== Combined Fore + Back ===")
print(Fore.BLACK   + Back.WHITE   + "Black on White")
print(Fore.RED     + Back.YELLOW + "Red on Yellow")
print(Fore.CYAN    + Back.MAGENTA+ "Cyan on Magenta")

print("\n=== Styles ===")
print(Style.DIM     + "Dim Text")
print(Style.NORMAL  + "Normal Text")
print(Style.BRIGHT  + "Bright Text")
print(Style.RESET_ALL + "Reset Style (Back to Normal)")

# Fancy combo
print("\n=== Full Combo ===")
print(Style.BRIGHT + Fore.YELLOW + Back.BLUE + "Bright Yellow Text on Blue Background")
