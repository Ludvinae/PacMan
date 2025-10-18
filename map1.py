WIDTH = 13
HEIGHT = 7

# Record all walls on the map
exteriorWalls = {
    (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (1,0), (1, 6), (2,0), (2,6),
    (3,0), (3,6), (4,0), (4,6), (5,0), (5,6), (6,0), (6,6), 
    (7,0), (7,6), (8,0), (8,6), (9,0), (9,6), (10,0), (10,6), 
    (11,0), (11,6), (12,0), (12,1), (12,2), (12,3), (12,4), (12,5), 
    (12,6)
}

interiorWalls = {
    (2,2), (2,5), (3,2), (3,3), (5,2), (5,4), (7,2), (7,4), (9,2), 
    (9,4), (11,3), (11,4), (12,1), (12,3)
}

WALLS = exteriorWalls.union(interiorWalls)


# Dictionnary with all infos on the map, imported in the main file
map = {
    "height": HEIGHT, "width": WIDTH, "walls": WALLS, "playerStartPosition": (6,3), 
    "ghostStartPosition": [], "maxScore": 0
}