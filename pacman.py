# Ahmet Oğuz Ergin
import os
import keyboard
import time
import sys


def initGameBoard():
    game_Board = []
    for i in range(0, ROW):
        row = []
        for j in range(0, COL):
            row.append(CELL_EMPTY)
        game_Board.append(row)

    return game_Board


def placeWallToBoard():
    for i in range(0, COL):
        game_Board[0][i] = CELL_WALL_HORIZONTAL
        game_Board[ROW - 1][i] = CELL_WALL_HORIZONTAL

    for i in range(0, ROW):
        game_Board[i][0] = CELL_WALL_VERTICAL
        game_Board[i][COL - 1] = CELL_WALL_VERTICAL

    for i in range(2, 3+1):
        game_Board[2][i] = CELL_WALL_HORIZONTAL
        game_Board[8][i] = CELL_WALL_HORIZONTAL

    for i in range(4, 5+1):
        game_Board[4][i] = CELL_WALL_HORIZONTAL
        game_Board[6][i] = CELL_WALL_HORIZONTAL

    for i in range(7, 12+1):
        game_Board[2][i] = CELL_WALL_HORIZONTAL
        game_Board[8][i] = CELL_WALL_HORIZONTAL

    for i in range(7, 8+1):
        game_Board[4][i] = CELL_WALL_HORIZONTAL
        game_Board[6][i] = CELL_WALL_HORIZONTAL

    for i in range(9, 10+1):
        game_Board[6][i] = CELL_WALL_HORIZONTAL

    for i in range(11, 12+1):
        game_Board[4][i] = CELL_WALL_HORIZONTAL
        game_Board[6][i] = CELL_WALL_HORIZONTAL

    for i in range(14, 15+1):
        game_Board[4][i] = CELL_WALL_HORIZONTAL
        game_Board[6][i] = CELL_WALL_HORIZONTAL

    for i in range(16, 17+1):
        game_Board[2][i] = CELL_WALL_HORIZONTAL
        game_Board[8][i] = CELL_WALL_HORIZONTAL

    for i in range(3, 4+1):
        game_Board[i][2] = CELL_WALL_VERTICAL

    for i in range(6, 7+1):
        game_Board[i][2] = CELL_WALL_VERTICAL

    for i in range(0, 2+1):
        game_Board[i][5] = CELL_WALL_VERTICAL

    for i in range(8, 9+1):
        game_Board[i][5] = CELL_WALL_VERTICAL

    game_Board[5][7] = CELL_WALL_VERTICAL
    game_Board[5][12] = CELL_WALL_VERTICAL

    for i in range(1, 2+1):
        game_Board[i][14] = CELL_WALL_VERTICAL

    for i in range(8, 9+1):
        game_Board[i][14] = CELL_WALL_VERTICAL

    for i in range(3, 4+1):
        game_Board[i][17] = CELL_WALL_VERTICAL

    for i in range(6, 7+1):
        game_Board[i][17] = CELL_WALL_VERTICAL


def displayBoard():
    for r in range(0, ROW):
        for c in range(0, COL):
            if(game_Board[r][c] == CELL_EMPTY):
                print("  ", end="")
            elif(game_Board[r][c] == CELL_WALL_HORIZONTAL):
                print("🟩", end="")
            elif(game_Board[r][c] == CELL_WALL_VERTICAL):
                print("🟩", end="")
            elif(game_Board[r][c] == CELL_PLAYER):
                print("🙂", end="")
            elif(game_Board[r][c] == CELL_MONSTER1 or CELL_MONSTER2 or CELL_MONSTER3):
                print("👻", end="")
        print()


def assingPlaceToPlayer():
    game_Board[locations["player"][0]][locations["player"][1]] = CELL_PLAYER


def assingPlaceToMonsters():
    # monster 1
    pass


def placeMonstersToBoard():
    game_Board[locations["monster1"][0]
               ][locations["monster1"][1]] = CELL_MONSTER1
    game_Board[locations["monster2"][0]
               ][locations["monster2"][1]] = CELL_MONSTER2
    game_Board[locations["monster3"][0]
               ][locations["monster3"][1]] = CELL_MONSTER3


def displayScore():
    print("             Score: " + str(score), end="\n")


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def on_key_press(event):
    # print(f"Key '{event.name}' pressed")
    global player_Direction
    global speed

    if event.name == 'esc':
        os._exit(0)

    if (event.name == 'up' or event.name == 'w') and game_Board[locations["player"][0] - 1][locations["player"][1]] == CELL_EMPTY:
        player_Direction = UP
    if (event.name == 'right' or event.name == 'd') and game_Board[locations["player"][0]][locations["player"][1] + 1] == CELL_EMPTY:
        player_Direction = RIGHT
    if (event.name == 'left' or event.name == 'a') and game_Board[locations["player"][0]][locations["player"][1] - 1] == CELL_EMPTY:
        player_Direction = LEFT
    if (event.name == 'down' or event.name == 's') and game_Board[locations["player"][0] + 1][locations["player"][1]] == CELL_EMPTY:
        player_Direction = DOWN

    if event.name == 'l':
        if(speed < 0.5):
            speed += 0.1

    if event.name == 'k':
        if(speed > 0.2):
            speed -= 0.1


def clearCurrentLocation():
    game_Board[locations["player"][0]][locations["player"][1]] = CELL_EMPTY


def movePlayer():
    clearCurrentLocation()

    if player_Direction == UP and game_Board[locations["player"][0] - 1][locations["player"][1]] == CELL_EMPTY:
        locations["player"][0] = locations["player"][0] - 1
    elif player_Direction == DOWN and game_Board[locations["player"][0] + 1][locations["player"][1]] == CELL_EMPTY:
        locations["player"][0] = locations["player"][0] + 1
    elif player_Direction == RIGHT and game_Board[locations["player"][0]][locations["player"][1] + 1] == CELL_EMPTY:
        locations["player"][1] = locations["player"][1] + 1
    elif player_Direction == LEFT and game_Board[locations["player"][0]][locations["player"][1] - 1] == CELL_EMPTY:
        locations["player"][1] = locations["player"][1] - 1

    assingPlaceToPlayer()


# MAIN--------
ROW = 11
COL = 20

CELL_EMPTY = 1000
CELL_WALL_VERTICAL = 1001
CELL_WALL_HORIZONTAL = 1002
CELL_PLAYER = 1003
CELL_MONSTER1 = 1004
CELL_MONSTER2 = 1005
CELL_MONSTER3 = 1006
UP = 1007
DOWN = 1008
LEFT = 1009
RIGHT = 1010

speed = 0.3
score = 0

player_Direction = None

locations = {"player": [7, 6], "monster1": [
    5, 8], "monster2": [5, 9], "monster3": [5, 10]}

keyboard.on_press(on_key_press)
game_Board = initGameBoard()
placeWallToBoard()
placeMonstersToBoard()
assingPlaceToPlayer()

clearScreen()
while True:
    displayScore()
    movePlayer()
    displayBoard()
    time.sleep(speed)
    clearScreen()
    pass
