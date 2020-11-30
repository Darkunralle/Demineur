import random as r

#Déclaration des variables
ligne, colonne = 0, 0
alive = 0
cpDrapeau = 0

#Création de la quantité de mine
def minecrea(taille):
    if taille == "Test":
        return 5
    if taille == "Practice":
        return 10
    if taille == "Medium":
        return 40
    if taille == "Hard":
        return 99

#Création du plateau et de la grille
def creation(taille):
    cplateau = []
    grille = []

    if taille == "Test":
        cplateau = [["*","*","*","*","*"],["*","*","*","*","*"],["*","*","*","*","*"],["*","*","*","*","*"],["*","*","*","*","*"],]
        grille = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],]
    if taille == "Practice":
        cplateau = [["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"]]
        grille = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    if taille == "Medium":
        cplateau = [["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]]
        grille = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    if taille == "Hard":
        cplateau = [["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]]
        grille = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    return cplateau, grille

print("Voici les difficultés disponibles :\nPractice 10x10 10 mine\nMedium 15x20 40 mine\nHard 20x30 99 mine")
taille = input("Selectionner votre difficulter : ")
print("Vous avez choisi la difficulté ",taille,"\n")

plateau, grille = creation(taille)

mine = minecrea(taille)

#Fonction d'affichage de la grille
def printInterface(interface):
    z=0
    print("   ", end="")
    for i in range(len(interface)):
        print(i,end="  ")
    print()
    for rows in interface:
        print(z, end="  ")
        for row in rows:
            print(row, end="  ")
        print("\n", end="")
        z+=1
    print("\n")

def firstmouve(interface, grille, mine):
    global ligne, colonne

    #Affichage du plateau au début
    printInterface(interface)

    #Premier mouvement avant initilisation des mines
    ligne = int(input("Entrer la ligne : "))
    colonne = int(input("Entrer la colonne : "))

    #Enregistrement du premier coup
    interface[ligne][colonne] = " "
  
    #Crée les case safe
    grille = safe(grille)
    #Génération des mines
    grille = minGen(grille,mine)
    #Initialise les compteurs a coter des mines
    grille = adjMine(grille)
    revealFirst(grille,interface)

def safe(grille):
    #Récupère les dimensions
    nbLigne = len(grille)
    nbColonne = len(grille[0])

    #Ligne 1
    grille[ligne][colonne] = "F"
    if colonne > 0:
        grille[ligne][colonne-1] = "s"
    if colonne < nbColonne-1 :
        grille[ligne][colonne+1] = "s"

    #Ligne -1
    if ligne > 0 :
        grille[ligne-1][colonne] = "s"
        if colonne > 0:
            grille[ligne-1][colonne-1] = "s"
        if colonne < nbColonne-1 :
            grille[ligne-1][colonne+1] = "s"

    #Ligne +2
    if ligne < nbLigne-1:
        grille[ligne+1][colonne] = "s"
        if colonne > 0:
            grille[ligne+1][colonne-1] = "s"
        if colonne < nbColonne-1 :
            grille[ligne+1][colonne+1] = "s"
    
    return grille

def adjMine(grille):
    #Récupération des limites
    nbLigne = len(grille)
    nbColonne = len(grille[0])

    #Parcours des listes
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

def minGen(grille,nbmine):
    mine = nbmine
    while mine > 0 :
        for mLigne in range(len(grille)-1):
            for mColonne in range(len(grille[mLigne])-1):
                if not grille[mLigne][mColonne] == "F" and not grille[mLigne][mColonne] == "s" and not grille[mLigne][mColonne] == "M" and mine > 0:
                    if r.randint(0,10) == 0 :
                        grille[mLigne][mColonne] = 'M'
                        mine -= 1
    return grille

def revealFirst(grille,plateau):
    for rligne in range(len(grille)):
        for rcolonne in range(len(grille[rligne])):
            if grille[rligne][rcolonne] == "s":
                plateau[rligne][rcolonne] = " "
    for i in range(10):
        rectif(grille,plateau)

def reveal(grille,ligne,colonne):
    nbLigne = len(grille)
    nbColonne = len(grille[0])
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if plateau[ligne][colonne] == " " or plateau[ligne][colonne] == "0" :
                if colonne > 0:
                    plateau[ligne][colonne-1] = str(grille[ligne][colonne-1])
                if colonne < nbColonne-1 :
                    plateau[ligne][colonne+1] = str(grille[ligne][colonne+1])

                if ligne > 0 :
                    plateau[ligne-1][colonne] = str(grille[ligne-1][colonne])
                    if colonne > 0:
                        plateau[ligne-1][colonne-1] = str(grille[ligne-1][colonne-1])
                    if colonne < nbColonne-1 :
                        plateau[ligne-1][colonne+1] = str(grille[ligne-1][colonne+1])

                if ligne < nbLigne-1:
                    plateau[ligne+1][colonne] = str(grille[ligne+1][colonne])
                    if colonne > 0:
                        plateau[ligne+1][colonne-1] = str(grille[ligne+1][colonne-1])
                    if colonne < nbColonne-1 :
                        plateau[ligne+1][colonne+1] = str(grille[ligne+1][colonne+1])
    
def rectif(grille,plateau):
    global ligne,colonne
    reveal(grille,ligne,colonne)
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if plateau[ligne][colonne] == "0" :
                reveal(grille,ligne,colonne)
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if plateau[ligne][colonne] == "0" or plateau[ligne][colonne] == "s" or plateau[ligne][colonne] == "F":
                plateau[ligne][colonne] = " "

def play(plateau,grille,mine):
    global alive, cpDrapeau
    printInterface(plateau)

    print("Il reste",str(mine-cpDrapeau),"mine sur la grille.")
    choix = input("Voulez vous révélez un Case ou placez un Drapeau : C / D : ")
    pLigne = int(input("Entrer la ligne : "))
    pColonne = int(input("Entrer la colonne : "))

    if choix == "C":
        if plateau[pLigne][pColonne] == "D":
            print("Vous venez de jouer sur un drapeau !\nPour le retirer selectionner D et les coordonnées d'un drapeau !")
            return play(plateau,grille,mine)
        else :
            if grille[pLigne][pColonne] == "M":
                alive = 1
            elif grille[pLigne][pColonne] == 0 :
                plateau[pLigne][pColonne] = str(grille[pLigne][pColonne])
                rectif(grille,plateau)
            else : plateau[pLigne][pColonne] = str(grille[pLigne][pColonne])
            if (mine - cpDrapeau) == 0 :
                alive = verifWin(plateau,mine)
                return alive
            else : return alive
    
    elif choix == "D":
        if plateau[pLigne][pColonne] == "D":
            plateau[pLigne][pColonne] = "*"
            cpDrapeau -= 1
        elif plateau[pLigne][pColonne] == "*":
            plateau[pLigne][pColonne] = "D"
            cpDrapeau += 1
        else : 
            print("Vous ne pouvez pas poser un drapeau sur une case découverte !") 
            return play(plateau,grille,mine)

        if (mine - cpDrapeau) == 0 :
            alive = verifWin(plateau,mine)
            return alive
        else : return alive
    else :
        print("Choix incorrecte !") 
        return play(plateau,grille,mine)

def verifWin(plateau,mine):
    compteur = 0
    for rows in plateau:
        for row in rows:
            if row == "*" or row == "D":
                compteur += 1
                print(compteur)
    print(mine)
    if compteur == mine :
        return 2
    else : return 0

def finalreveal(plateau, grille):
    for f in range(len(plateau)):
        for g in range(len(plateau)):
            if grille[f][g] == "M":
                plateau[f][g] = "M"
    printInterface(plateau)


firstmouve(plateau, grille, mine)
while alive == 0:
    play(plateau,grille,mine)
if alive == 1 :
    print("Vous avez perdu")
    finalreveal(plateau, grille)
else : print("Vous avez gagner GG")