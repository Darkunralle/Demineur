import random as r

practice = [["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"]]
grille = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
mine = 10
ligne, colonne = 0, 0
#Fonction d'affichage de la grille
def printInterface(interface):
    for cp in range(len(interface)):
        print(interface[cp])
    print("***************************************")

def printGrille(grille):
    for cp in range(len(grille)):
        print(grille[cp])
    print("***************************************")

def firstmouve(interface):
    global grille, mine, ligne, colonne

    #print grille
    printInterface(interface)

    ligne = int(input("Entrer la ligne : "))
    colonne = int(input("Entrer la colonne : "))

    #print grille
    interface[ligne][colonne] = " "

    printInterface(interface)

    grille = safe(grille)

    grille = minGen(grille,mine)
    grille = adjMine(grille)
    printGrille(grille)
    revealFirst()
    printInterface(interface)

def safe(grille):
    nbLigne = len(grille)
    nbColonne = len(grille[0])

    grille[ligne][colonne] = "F"
    if colonne > 0:
        grille[ligne][colonne-1] = "s"
    if colonne < nbColonne-1 :
        grille[ligne][colonne+1] = "s"

    if ligne > 0 :
        grille[ligne-1][colonne] = "s"
        if colonne > 0:
            grille[ligne-1][colonne-1] = "s"
        if colonne < nbColonne-1 :
            grille[ligne-1][colonne+1] = "s"

    if ligne < nbLigne-1:
        grille[ligne+1][colonne] = "s"
        if colonne > 0:
            grille[ligne+1][colonne-1] = "s"
        if colonne < nbColonne-1 :
            grille[ligne+1][colonne+1] = "s"
    
    return grille

def adjMine(grille):
    nbLigne = len(grille)
    nbColonne = len(grille[0])
    for mLigne in range(len(grille)):
            for mColonne in range(len(grille[mLigne])):
                if grille[mLigne][mColonne] == "M":
                    if mColonne > 0:
                        if not grille[mLigne][mColonne-1] == "M":
                            if grille[mLigne][mColonne-1] == "s":
                                grille[mLigne][mColonne-1] = 0 
                            grille[mLigne][mColonne-1] += 1 
                    if mColonne < nbColonne-1 :
                        if not grille[mLigne][mColonne+1] == "M":
                            if grille[mLigne][mColonne+1] == "s":
                                grille[mLigne][mColonne+1] = 0
                            grille[mLigne][mColonne+1] += 1

                    if mLigne > 0 :
                        if not grille[mLigne-1][mColonne] == "M":
                            if grille[mLigne-1][mColonne] == "s":
                                grille[mLigne-1][mColonne] = 0
                            grille[mLigne-1][mColonne] += 1
                        if mColonne > 0:
                            if not grille[mLigne-1][mColonne-1] == "M":
                                if grille[mLigne-1][mColonne-1] == "s":
                                    grille[mLigne-1][mColonne-1] = 0
                                grille[mLigne-1][mColonne-1] += 1
                        if mColonne < nbColonne-1 :
                            if not grille[mLigne-1][mColonne+1] == "M":
                                if grille[mLigne-1][mColonne+1] == "s":
                                    grille[mLigne-1][mColonne+1] = 0
                                grille[mLigne-1][mColonne+1] += 1

                    if mLigne < nbLigne-1:
                        if not grille[mLigne+1][mColonne] == "M":
                            if grille[mLigne+1][mColonne] == "s":
                                grille[mLigne+1][mColonne] = 0
                            grille[mLigne+1][mColonne] += 1
                        if mColonne > 0:
                            if not grille[mLigne+1][mColonne-1] == "M":
                                if grille[mLigne+1][mColonne-1] == "s":
                                    grille[mLigne+1][mColonne-1] = 0
                                grille[mLigne+1][mColonne-1] += 1
                        if mColonne < nbColonne-1 :
                            if not grille[mLigne+1][mColonne+1] == "M":
                                if grille[mLigne+1][mColonne+1] == "s":
                                    grille[mLigne+1][mColonne+1] = 0
                                grille[mLigne+1][mColonne+1] += 1
    return grille

def minGen(grille,mine):
    while mine > 0 :
        for mLigne in range(len(grille)-1):
            for mColonne in range(len(grille[mLigne])-1):
                if not grille[mLigne][mColonne] == "F" and not grille[mLigne][mColonne] == "s" and not grille[mLigne][mColonne] == "M" and mine > 0:
                    if r.randint(0,10) == 0 :
                        grille[mLigne][mColonne] = 'M'
                        mine -= 1
    return grille

def revealFirst():
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if grille[ligne][colonne] == "s":
                practice[ligne][colonne] = " "
    reveal()

def reveal():
    nbLigne = len(grille)
    nbColonne = len(grille[0])
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if practice[ligne][colonne] == " " or practice[ligne][colonne] == 0 :
                if colonne > 0:
                    practice[ligne][colonne-1] = grille[ligne][colonne-1]
                if colonne < nbColonne-1 :
                    practice[ligne][colonne+1] = grille[ligne][colonne+1]

                if ligne > 0 :
                    practice[ligne-1][colonne] = grille[ligne-1][colonne]
                    if colonne > 0:
                        practice[ligne-1][colonne-1] = grille[ligne-1][colonne-1]
                    if colonne < nbColonne-1 :
                        practice[ligne-1][colonne+1] = grille[ligne-1][colonne+1]

                if ligne < nbLigne-1:
                    practice[ligne+1][colonne] = grille[ligne+1][colonne]
                    if colonne > 0:
                        practice[ligne+1][colonne-1] = grille[ligne+1][colonne-1]
                    if colonne < nbColonne-1 :
                        practice[ligne+1][colonne+1] = grille[ligne+1][colonne+1]
    
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if practice[ligne][colonne] == 0 or practice[ligne][colonne] == "s" or practice[ligne][colonne] == "F":
                practice[ligne][colonne] = " "
    
    


firstmouve(practice)
