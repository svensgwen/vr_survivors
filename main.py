
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

# ---------------------------------------------------- VARIABLES ----------------------------------------------------

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
