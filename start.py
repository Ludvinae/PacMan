# Functions to get the starting conditions, run once at the start of a new game
def generatePlayer(map):
    symbol = input("Voulez-vous jouer avec Pacman (M), Pacwoman (W) ou Pacperson (P) ? ").upper()
    if symbol != "P" and symbol != "W" and symbol != "M":
        symbol = "P"
    return {"position": map["playerStartPosition"], "symbol": symbol, "score": 0, "level": 1}

def generateGhosts(map):
    return [{"position": position, "isOnGum": True, "movesRandomly": False} for position in map["ghostStartPosition"]]

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