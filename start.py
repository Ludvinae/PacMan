# Functions to get the starting conditions, run once at the start of a new map


def generateGhosts(map):
    return [{"position": position, "isOnGum": True, "movesRandomly": True} for position in map["ghostStartPosition"]]


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