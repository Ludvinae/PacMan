import os

gameContinue = True

def display(grid, player):
    # Efface l'affichage precedent
    clearScreen()
    print("__________________________________")
    print(f"| Level: {player["level"]}      | Score: {player["score"]}      |")
    print("|________________________________|")

    for y in range(len(grid)):
        print()
        for x in range(len(grid[y])):
            print(grid[y][x], end="")

        
def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def gameEnd(type):
    global gameContinue
    if type == "over":
        os.system("cls" if os.name == "nt" else "clear")
        print("____________________________________")
        print("|          GAME OVER !             |")
        print("|__________________________________|")
        gameContinue = False
    elif type == "win":
        os.system("cls" if os.name == "nt" else "clear")
        print("____________________________________")
        print("|           YOU WON !             |")
        print("|__________________________________|")
        gameContinue = False


def continuePlaying():
    global gameContinue
    playerInput = input("Voulez-vous continuer à jouer? (Oui ou Non): ").lower().strip()
    if not playerInput:
        playerInput = "o" 
    if playerInput[0] == "o":
        gameContinue = True
        return True
    
    return False
        