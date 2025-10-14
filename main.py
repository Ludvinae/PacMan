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
        move(currentMap, grid, player)


def display(grid):
    # Efface l'affichage precedent
    os.system("cls" if os.name == "nt" else "clear")

    for y in range(len(grid)):
        print()
        for x in range(len(grid[y])):
            print(grid[y][x], end="")


def move(map, grid, player):
    x, y = player["position"]
    grid[y][x] = " "
    print()
    match input("Movement (ZQSD): ").lower():
        case "z":
            if isValidMove(x, y - 1, map):
                player["position"] = (x,y-1)                
        case "q":
            if isValidMove(x - 1, y, map):
                player["position"] = (x-1,y) 
        case "s":
            if isValidMove(x, y + 1, map):
                player["position"] = (x,y+1) 
        case "d":
            if isValidMove(x + 1, y, map):
                player["position"] = (x+1,y) 
        case _:
            player["position"] = (x,y)

    grid[player["position"][1]][player["position"][0]] = player["symbol"]

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
    for y in range(map["height"]):
        for x in range(map["width"]):
            if (x,y) in map["walls"]:
                grid[y][x] = "#"
            elif (x,y) == map["playerStartPosition"]:
                grid[y][x] = player["symbol"]
            elif (x,y) in map["ghostStartPosition"]:
                grid[y][x] = "G"

    return grid


# Execution de la fonction principale
main()