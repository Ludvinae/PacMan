import map1, map2, map3

mapList = [map1.map, map2.map, map3.map]

def getMap(level):
    currentMap = mapList[level - 1]
    currentMap["maxScore"] = setMaxScore(currentMap)

    return currentMap

def setMaxScore(map):
    mapArea = map["height"] * map["width"]
    wallArea = len(map["walls"])

    return mapArea - wallArea - 1