import os
from map import map1
from math import sqrt
from random import choices
import start


gameContinue = True

def main():
    currentMap = map1
    player = start.generatePlayer(currentMap)
    ghosts = start.generateGhosts(currentMap)
    grid = start.generateMap(currentMap, player)

    
    # Boucle de jeu principale
    while gameContinue:
        display(grid, player)
        ghostMove(ghosts, player, currentMap, grid)
        if gameContinue:
            move(currentMap, grid, player)
        

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
    ghostPositions = set()
    for ghost in ghosts:
        ghostPositions.add(ghost["position"])

    for ghost in ghosts:
        ghostPositions.remove(ghost["position"])
        x, y = ghost["position"]
        if ghost["isOnGum"]:
            grid[y][x] = "."
        else:
            grid[y][x] = " "

        validPositions = testWallPosition(x, y, map, ghostPositions)

        if len(validPositions) >= 3:
            validPositions = choices(validPositions, k=(len(validPositions) -1))
        x, y = getDistance(validPositions, player)

        ghost["position"] = (x, y)
        ghostPositions.add(ghost["position"])
        if grid[y][x] == player["symbol"]:
            gameEnd("over")
        if grid[y][x] == ".":
            ghost["isOnGum"] = True
        else:
            ghost["isOnGum"] = False
        grid[y][x] = "G"



def testWallPosition(x, y, map, ghostPositions : set):
    positions = []
    
    for i in range(-1, 2):
        if i != 0:
            pos = (x+i, y)
            if pos not in map["walls"] and pos not in ghostPositions:
                positions.append(pos)
            pos = (x, y+i)
            if pos not in map["walls"] and pos not in ghostPositions:
                positions.append(pos)
    
    return positions

def euclidianDistance(position1 : tuple, position2 : tuple):
    ghostX, ghostY = position1
    playerX, playerY = position2
    return sqrt(((ghostX - playerX) ** 2) + ((ghostY - playerY) ** 2))

def getDistance(moves : list, player):
    bestMove = moves[0]
    minDistance = euclidianDistance(moves[0], player["position"])
    for move in moves[1:]:
        distance = euclidianDistance(move, player["position"])
        if distance < minDistance:
            minDistance = distance
            bestMove = move
    
    return bestMove

        
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



# Execution de la fonction principale
main()