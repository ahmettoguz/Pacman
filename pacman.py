# Ahmet Oğuz Ergin
import os
import keyboard
import time
import random


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
            elif(game_Board[r][c] == CELL_FOOD):
                print("🍕", end="")
            elif(game_Board[r][c] == CELL_MONSTER):
                print("👻", end="")
        print()


def assingPlaceToPlayer():
    game_Board[locations["player"][0]][locations["player"][1]] = CELL_PLAYER


def assignPlaceToMonster():
    game_Board[locations["monster1"][0]
               ][locations["monster1"][1]] = CELL_MONSTER
    game_Board[locations["monster2"][0]
               ][locations["monster2"][1]] = CELL_MONSTER
    game_Board[locations["monster3"][0]
               ][locations["monster3"][1]] = CELL_MONSTER


def assingPlaceToMonsters():
    # monster 1
    pass


def placeMonstersToBoard():
    game_Board[locations["monster1"][0]
               ][locations["monster1"][1]] = CELL_MONSTER
    game_Board[locations["monster2"][0]
               ][locations["monster2"][1]] = CELL_MONSTER
    game_Board[locations["monster3"][0]
               ][locations["monster3"][1]] = CELL_MONSTER


def displayTitle():
    if speed == 0.1:
        speedTitle = "Fast"
    elif speed == 0.3:
        speedTitle = "Normal"
    elif speed == 0.5:
        speedTitle = "Slow"

    print("        Speed : " + speedTitle +
          " - Score: " + str(score), end="\n")


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def initToStartAgain():
    global directions
    global locations
    global speed
    global score
    global game_Status
    global game_Board

    speed = 0.3
    score = 0

    directions = {"player": None, "monster1": None,
                  "monster2": None, "monster3": None}

    locations = {"player": [7, 10], "monster1": [
        5, 8], "monster2": [5, 9], "monster3": [5, 10]}

    game_Board = initGameBoard()
    initScoreToBoard()
    placeWallToBoard()
    placeMonstersToBoard()
    assingPlaceToPlayer()


def on_key_press(event):
    # print(f"Key '{event.name}' pressed")
    global directions
    global speed
    global game_Status

    if event.name == 'esc':
        os._exit(0)

    elif event.name == 'space':
        if game_Status == END:
            initToStartAgain()

        game_Status = PLAY

    elif (event.name == 'up' or event.name == 'w') and (game_Board[locations["player"][0] - 1][locations["player"][1]] == CELL_EMPTY or game_Board[locations["player"][0] - 1][locations["player"][1]] == CELL_FOOD):
        directions["player"] = UP
    elif (event.name == 'right' or event.name == 'd') and (game_Board[locations["player"][0]][locations["player"][1] + 1] == CELL_EMPTY or game_Board[locations["player"][0]][locations["player"][1] + 1] == CELL_FOOD):
        directions["player"] = RIGHT
    elif (event.name == 'down' or event.name == 's') and (game_Board[locations["player"][0] + 1][locations["player"][1]] == CELL_EMPTY or game_Board[locations["player"][0] + 1][locations["player"][1]] == CELL_FOOD):
        directions["player"] = DOWN
    elif (event.name == 'left' or event.name == 'a') and (game_Board[locations["player"][0]][locations["player"][1] - 1] == CELL_EMPTY or game_Board[locations["player"][0]][locations["player"][1] - 1] == CELL_FOOD):
        directions["player"] = LEFT

    elif event.name == '-':
        if(speed == 0.1):
            speed = 0.3
        elif(speed == 0.3):
            speed = 0.5

    elif event.name == '+':
        if(speed == 0.5):
            speed = 0.3
        elif(speed == 0.3):
            speed = 0.1


def clearCurrentLocation():
    game_Board[locations["player"][0]][locations["player"][1]] = CELL_EMPTY


def clearMonsterLocation(m):
    game_Board[locations[m][0]][locations[m][1]] = CELL_EMPTY


def movePlayer():
    clearCurrentLocation()

    if directions["player"] == UP and (game_Board[locations["player"][0] - 1][locations["player"][1]] == CELL_EMPTY or game_Board[locations["player"][0] - 1][locations["player"][1]] == CELL_FOOD):
        locations["player"][0] = locations["player"][0] - 1
    elif directions["player"] == RIGHT and (game_Board[locations["player"][0]][locations["player"][1] + 1] == CELL_EMPTY or game_Board[locations["player"][0]][locations["player"][1] + 1] == CELL_FOOD):
        locations["player"][1] = locations["player"][1] + 1
    elif directions["player"] == DOWN and (game_Board[locations["player"][0] + 1][locations["player"][1]] == CELL_EMPTY or game_Board[locations["player"][0] + 1][locations["player"][1]] == CELL_FOOD):
        locations["player"][0] = locations["player"][0] + 1
    elif directions["player"] == LEFT and (game_Board[locations["player"][0]][locations["player"][1] - 1] == CELL_EMPTY or game_Board[locations["player"][0]][locations["player"][1] - 1] == CELL_FOOD):
        locations["player"][1] = locations["player"][1] - 1

    assingPlaceToPlayer()


def initScoreToBoard():
    game_Board[3][1] = CELL_FOOD
    game_Board[1][3] = CELL_FOOD

    game_Board[7][1] = CELL_FOOD
    game_Board[9][3] = CELL_FOOD

    game_Board[5][5] = CELL_FOOD

    game_Board[1][8] = CELL_FOOD
    game_Board[1][11] = CELL_FOOD

    game_Board[9][8] = CELL_FOOD
    game_Board[9][11] = CELL_FOOD

    game_Board[5][14] = CELL_FOOD

    game_Board[1][16] = CELL_FOOD
    game_Board[3][18] = CELL_FOOD

    game_Board[9][16] = CELL_FOOD
    game_Board[7][18] = CELL_FOOD


def addFood():
    r = random.randint(1, ROW-1)
    c = random.randint(1, COL-1)

    while game_Board[r][c] != CELL_EMPTY:
        r = random.randint(1, ROW-1)
        c = random.randint(1, COL-1)

    game_Board[r][c] = CELL_FOOD


def increaseScore():
    global score

    if (directions["player"] == UP and game_Board[locations["player"][0] - 1][locations["player"][1]] == CELL_FOOD) or (directions["player"] == RIGHT and game_Board[locations["player"][0]][locations["player"][1] + 1] == CELL_FOOD) or (directions["player"] == DOWN and game_Board[locations["player"][0] + 1][locations["player"][1]] == CELL_FOOD) or (directions["player"] == LEFT and game_Board[locations["player"][0]][locations["player"][1] - 1] == CELL_FOOD):
        score += 1
        addFood()


def checkLose():
    global game_Status

    # player movement
    if (directions["player"] == UP and game_Board[locations["player"][0] - 1][locations["player"][1]] == CELL_MONSTER) or (directions["player"] == RIGHT and game_Board[locations["player"][0]][locations["player"][1] + 1] == CELL_MONSTER) or (directions["player"] == DOWN and game_Board[locations["player"][0] + 1][locations["player"][1]] == CELL_MONSTER) or (directions["player"] == LEFT and game_Board[locations["player"][0]][locations["player"][1] - 1] == CELL_MONSTER):
        game_Status = END

    # monster movement
    for index in range(1, 3 + 1):
        m = "monster" + str(index)

        if (directions[m] == UP and game_Board[locations[m][0] - 1][locations[m][1]] == CELL_PLAYER) or (directions[m] == RIGHT and game_Board[locations[m][0]][locations[m][1] + 1] == CELL_PLAYER) or (directions[m] == DOWN and game_Board[locations[m][0] + 1][locations[m][1]] == CELL_PLAYER) or (directions[m] == LEFT and game_Board[locations[m][0]][locations[m][1] - 1] == CELL_PLAYER):
            game_Status = END


def moveMonsters():
    for index in range(1, 3 + 1):
        m = "monster" + str(index)

        clearMonsterLocation(m)

        if directions[m] == UP and (game_Board[locations[m][0] - 1][locations[m][1]] == CELL_EMPTY or game_Board[locations[m][0] - 1][locations[m][1]] == CELL_FOOD or game_Board[locations[m][0] - 1][locations[m][1]] == CELL_PLAYER or game_Board[locations[m][0] - 1][locations[m][1]] == CELL_MONSTER):
            locations[m][0] = locations[m][0] - 1
        elif directions[m] == RIGHT and (game_Board[locations[m][0]][locations[m][1] + 1] == CELL_EMPTY or game_Board[locations[m][0]][locations[m][1] + 1] == CELL_FOOD or game_Board[locations[m][0]][locations[m][1] + 1] == CELL_PLAYER or game_Board[locations[m][0]][locations[m][1] + 1] == CELL_MONSTER):
            locations[m][1] = locations[m][1] + 1
        elif directions[m] == DOWN and (game_Board[locations[m][0] + 1][locations[m][1]] == CELL_EMPTY or game_Board[locations[m][0] + 1][locations[m][1]] == CELL_FOOD or game_Board[locations[m][0] + 1][locations[m][1]] == CELL_PLAYER or game_Board[locations[m][0] + 1][locations[m][1]] == CELL_MONSTER):
            locations[m][0] = locations[m][0] + 1
        elif directions[m] == LEFT and (game_Board[locations[m][0]][locations[m][1] - 1] == CELL_EMPTY or game_Board[locations[m][0]][locations[m][1] - 1] == CELL_FOOD or game_Board[locations[m][0]][locations[m][1] - 1] == CELL_PLAYER or game_Board[locations[m][0]][locations[m][1] - 1] == CELL_MONSTER):
            locations[m][1] = locations[m][1] - 1

        assignPlaceToMonster()


# MAIN--------
ROW = 11
COL = 20

CELL_EMPTY = 1000
CELL_WALL_VERTICAL = 1001
CELL_WALL_HORIZONTAL = 1002
CELL_PLAYER = 1003
CELL_MONSTER = 1004
UP = 1007
DOWN = 1008
LEFT = 1009
RIGHT = 1010
CELL_FOOD = 1011
PLAY = 1012
END = 1013
START = 1014

speed = 0.3
score = 0
game_Status = START

directions = {"player": None, "monster1": DOWN,
              "monster2": None, "monster3": None}

# directions = {"player": None, "monster1": None,
#               "monster2": None, "monster3": None}


# locations = {"player": [7, 10], "monster1": [
#     5, 8], "monster2": [5, 9], "monster3": [5, 10]} 
locations = {"player": [7, 6], "monster1": [
    2, 6], "monster2": [5, 9], "monster3": [5, 10]}

keyboard.on_press(on_key_press)
game_Board = initGameBoard()
initScoreToBoard()
placeWallToBoard()
placeMonstersToBoard()
assingPlaceToPlayer()


clearScreen()
while True:
    checkLose()
    if game_Status == PLAY:
        increaseScore()
        displayTitle()
        moveMonsters()
        movePlayer()
        displayBoard()

    elif game_Status == END:
        print("Game is over with score: " + str(score))
        print("Press space to play again.")

    elif game_Status == START:
        print("Press space to start game.")
        print("Press esc to end game..")
        print("Good Luck...")
    time.sleep(speed)
    clearScreen()


# speed can be changed.
# esc terminates program directly
# foods generated automatically
