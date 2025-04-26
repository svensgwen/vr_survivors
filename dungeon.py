import curses

# Symbols
PLAYER = '@'
WALL = '#'
FLOOR = ' '
ENEMY = 'Ω'
CHEST = '≡'
DOOR = '⌂'
OTHER = ["☠", "⎔"]

# Initial map (5x5 test)
map_data = {}
[
    "####################",
    "#       #     #    #",
    "D    #     #       #",
    "# ☠   #         @  #",
    "####################"
]

def main(stdscr):
    curses.curs_set(0)  # hide cursor
    stdscr.nodelay(True)
    stdscr.timeout(100)

    player_y, player_x = 1, 2

    while True:
        stdscr.clear()

        # Draw map
        for y, row in enumerate(map_data):
            stdscr.addstr(y, 0, row)

        stdscr.addstr(6, 0, f"Health: 103 / 103")

        key = stdscr.getch()

        dy, dx = 0, 0
        if key == curses.KEY_UP:
            dy = -1
        elif key == curses.KEY_DOWN:
            dy = 1
        elif key == curses.KEY_LEFT:
            dx = -1
        elif key == curses.KEY_RIGHT:
            dx = 1
        elif key == ord('q'):
            break

        new_y = player_y + dy
        new_x = player_x + dx

        if map_data[new_y][new_x] == FLOOR:
            # Replace current player pos with floor
            map_data[player_y] = map_data[player_y][:player_x] + FLOOR + map_data[player_y][player_x+1:]
            # Move player
            player_y, player_x = new_y, new_x
            map_data[player_y] = map_data[player_y][:player_x] + PLAYER + map_data[player_y][player_x+1:]

        stdscr.refresh()

curses.wrapper(main)
