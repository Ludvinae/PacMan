from map import map1
import start
from player import playerMove
from ghost import ghostMove
import display


def main():
    currentMap = map1
    player = start.generatePlayer(currentMap)
    ghosts = start.generateGhosts(currentMap)
    grid = start.generateMap(currentMap, player)
    
    # Boucle de jeu principale
    while display.gameContinue:
        display.display(grid, player)
        ghostMove(ghosts, player, currentMap, grid)
        if display.gameContinue:
            playerMove(currentMap, grid, player)
        

# Execution de la fonction principale
main()