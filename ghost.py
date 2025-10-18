from math import sqrt
from random import choices
from display import gameEnd

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