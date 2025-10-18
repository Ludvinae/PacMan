from map import map1
import start
from player import playerMove, generatePlayer
from ghost import ghostMove
import display


def main():
    # Ask player for his prefered symbol
    player = generatePlayer()
    display.clearScreen()

    # Boucle de jeu principale
    while True:
        # Generate a new map
        currentMap = map1
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
                
        
        if not display.continuePlaying():
            break


# Execution de la fonction principale
main()