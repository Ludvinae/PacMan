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
        # Utilise la liste de listes grid pour afficher l'etat actuel du jeu
        display.display(grid, player)
        # Décide des mouvements de chaque ghost en fonction de la distance avec le player
        ghostMove(ghosts, player, currentMap, grid)
        if display.gameContinue:
            # Demande au joueur son choix de mouvement et update le grid en fonction
            playerMove(currentMap, grid, player)
        

# Execution de la fonction principale
main()