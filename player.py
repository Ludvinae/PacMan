from display import gameEnd


def playerMove(map, grid, player):
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