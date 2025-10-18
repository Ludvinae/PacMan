from sys import argv
from time import sleep
from mapSelector import getMap
import start
from player import playerMove, generatePlayer
from ghost import ghostMove
import display


def main():
    # check for command line arguments to set player starting level
    if len(argv) > 1:
        if argv[1].isdigit():
            level = int(argv[1])
    else:
        level = 1

    # Ask player for his prefered symbol
    player = generatePlayer(level)
    display.clearScreen()

    # Boucle de jeu principale
    while True:
        # Generate a new map
        currentMap = getMap(player["level"])
        player["position"] = currentMap["playerStartPosition"]
        ghosts = start.generateGhosts(currentMap)
        grid = start.generateMap(currentMap, player)

        while display.gameContinue:
            # Utilise la liste de listes grid pour afficher l'etat actuel du jeu
            display.display(grid, player)
            # Demande au joueur son choix de mouvement et update le grid en fonction
            playerMove(currentMap, grid, player)
            if display.gameContinue:
                display.display(grid, player)
                # Décide des mouvements de chaque ghost en fonction de la distance avec le player
                ghostMove(ghosts, player, currentMap, grid)
                if len(ghosts) > 0:
                    sleep(0.15)
                
        
        if not display.continuePlaying():
            break


# Execution de la fonction principale
main()