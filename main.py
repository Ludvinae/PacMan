import os
from map import map1


def main():
    currentMap = map1
    player = generatePlayer(currentMap)
    ghosts = generateGhosts(currentMap)
    grid = generateMap(currentMap, player)

    # Boucle de jeu principale
    while True:
        display(grid)
        break


def display(grid):
    # Efface l'affichage precedent
    os.system("cls" if os.name == "nt" else "clear")

    for x in range(len(grid)):
        print()
        for y in range(len(grid[x])):
            print(grid[x][y], end="")


def move(grid, player):
    x, y = player["position"]
    match input("Movement (ZQSD): ").lower():
        case "z":
            if isValidMove(x, y - 1, grid):
                pass
        case "q":
            if isValidMove(x - 1, y, grid):
                pass
        case "s":
            if isValidMove(x, y + 1, grid):
                pass
        case "d":
            if isValidMove(x + 1, y, grid):
                pass

def isValidMove(x, y, map):
    if (x,y) not in map["walls"]:
        return True
    return False


# Functions to get the starting conditions, run once at the start of a new game
def generatePlayer(map):
    symbol = input("Voulez-vous jouer avec Pacman (P) ou avec Pacwoman (W)?").upper()
    if symbol != "P" or symbol != "W":
        symbol = "P"
    return {"position": map["playerStartPosition"], "symbol": symbol, "score": 0, "level": 1}

def generateGhosts(map):
    return [{"position": position, "isOnGum": True} for position in map["ghostStartPosition"]]

def generateMap(map, player):
    grid = [["."]*map["width"] for _ in range(map["height"])]
    for x in range(map["height"]):
        for y in range(map["width"]):
            if (y,x) in map["walls"]:
                grid[x][y] = "#"
            elif (y,x) == map["playerStartPosition"]:
                grid[x][y] = player["symbol"]
            elif (y,x) in map["ghostStartPosition"]:
                grid[x][y] = "G"

    return grid


# Execution de la fonction principale
main()