import os
from map import map1
from random import choice


gameContinue = True

def main():
    currentMap = map1
    player = generatePlayer(currentMap)
    ghosts = generateGhosts(currentMap)
    grid = generateMap(currentMap, player)

    
    # Boucle de jeu principale
    while gameContinue:
        display(grid, player)
        move(currentMap, grid, player)
        if gameContinue:
            ghostMove(ghosts, player, currentMap, grid)
        

def display(grid, player):
    # Efface l'affichage precedent
    os.system("cls" if os.name == "nt" else "clear")
    print("__________________________________")
    print(f"| Level: {player["level"]}      | Score: {player["score"]}      |")
    print("|________________________________|")

    for y in range(len(grid)):
        print()
        for x in range(len(grid[y])):
            print(grid[y][x], end="")


def move(map, grid, player):
    x, y = player["position"]
    grid[y][x] = " "
    print()
    match input("Movement (ZQSD): ").lower()[:1]:
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

    newX = player["position"][0]
    newY = player["position"][1]
    if grid[newY][newX] == "G":
        gameEnd("over")
    else:
        if grid[newY][newX] == ".":
            player["score"] += 1
            if player["score"] == map["maxScore"]:
                gameEnd("win")  
        grid[newY][newX] = player["symbol"]

def isValidMove(x, y, map):
    if (x,y) not in map["walls"]:
        return True
    return False

def ghostMove(ghosts, player, map, grid):
    for ghost in ghosts:
        x, y = ghost["position"]
        if ghost["isOnGum"]:
            grid[y][x] = "."
        else:
            grid[y][x] = " "
        validPositions = testPosition(x, y, map)
        x, y = choice(validPositions)
        ghost["position"] = (x, y)
        if grid[y][x] == player["symbol"]:
            gameEnd("over")
        if grid[y][x] == ".":
            ghost["isOnGum"] = True
        else:
            ghost["isOnGum"] = False
        grid[y][x] = "G"


def testPosition(x, y, map):
    positions = []
    for i in range(-1, 2):
        if i != 0:
            pos = (x+i, y)
            if pos not in map["walls"]:
                positions.append(pos)
            pos = (x, y+i)
            if pos not in map["walls"]:
                positions.append(pos)
    
    return positions
        
def gameEnd(type):
    global gameContinue
    if type == "over":
        os.system("cls" if os.name == "nt" else "clear")
        print("____________________________________")
        print("|          GAME OVER !             |")
        print("|__________________________________|")
        gameContinue = False
    elif type == "win":
        os.system("cls" if os.name == "nt" else "clear")
        print("____________________________________")
        print("|           YOU WON !             |")
        print("|__________________________________|")
        gameContinue = False


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