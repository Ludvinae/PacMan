from map import map1


def main():
    currentMap = map1
    grid = generateMap(currentMap)
    while True:
        display(grid)
        break


def display(grid):
    for x in range(len(grid)):
        print()
        for y in range(len(grid[x])):
            print(grid[x][y], end="")


def generateMap(map):
    grid = [["."]*map["width"] for _ in range(map["height"])]
    for x in range(map["height"]):
        for y in range(map["width"]):
            if (y,x) in map["walls"]:
                grid[x][y] = "#"
            elif (y,x) == map["playerStartPosition"]:
                grid[x][y] = "P"
            elif (y,x) in map["ghostStartPosition"]:
                grid[x][y] = "G"

    return grid

main()