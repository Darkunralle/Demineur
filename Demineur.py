import random as r

#Déclaration des variables
ligne, colonne = 0, 0
alive = 0
cpDrapeau = 0

#Création de la quantité de mine
def minecrea(taille):
    if taille == "Practice":
        return 10
    if taille == "Medium":
        return 40
    if taille == "Hard":
        return 99
#Création du plateau et de la grille
def creation(taille):
    cplateau = []
    case=[]

    if taille == "Practice":
        nbcolonne = 10
        nbligne = 10
    if taille == "Medium":
        nbcolonne = 15
        nbligne = 20
    if taille == "Hard":
        nbcolonne = 20
        nbligne = 30

    for z in range(nbcolonne):
        case.append("*")

    for i in range(nbligne):
        cplateau.append(case)
    
    return cplateau

print("Voici les difficultés disponibles :\nPractice 10x10 10 mine\nMedium 15x20 40 mine\nHard 20x30 99 mine")
taille = input("Selectionner votre difficulter : ")
print("Vous avez choisi la difficulté ",taille)

plateau = creation(taille)
grille = creation(taille)
mine = minecrea(taille)

#Fonction d'affichage de la grille
def printInterface(interface):
    for cp in range(len(interface)):
        print(interface[cp])
    print("***************************************")

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
    printInterface(interface)

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

def minGen(grille,mine):
    while mine > 0 :
        for mLigne in range(len(grille)-1):
            for mColonne in range(len(grille[mLigne])-1):
                if not grille[mLigne][mColonne] == "F" and not grille[mLigne][mColonne] == "s" and not grille[mLigne][mColonne] == "M" and mine > 0:
                    if r.randint(0,10) == 0 :
                        grille[mLigne][mColonne] = 'M'
                        mine -= 1
    return grille

def revealFirst(grille,plateau):
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if grille[ligne][colonne] == "s":
                plateau[ligne][colonne] = " "
    for i in range(5):
        rectif()

def reveal():
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
    
def rectif():
    reveal()
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if plateau[ligne][colonne] == "0" :
                reveal()
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if plateau[ligne][colonne] == "0" or plateau[ligne][colonne] == "s" or plateau[ligne][colonne] == "F":
                plateau[ligne][colonne] = " "

def play():
    global alive, plateau, cpDrapeau

    choix = input("Voulez vous révélez un case ou placez un drapeau : C / D")

    pLigne = int(input("Entrer la ligne : "))
    pColonne = int(input("Entrer la colonne : "))

    if choix == "C":
        if plateau[pLigne][pColonne] == "D":
            return play()
        else :
            if grille[pLigne][pColonne] == "M":
                alive = 1
            elif grille[pLigne][pColonne] == 0 :
                plateau[pLigne][pColonne] = str(grille[pLigne][pColonne])
                rectif()
            else : plateau[pLigne][pColonne] = str(grille[pLigne][pColonne])

            printInterface(plateau)

            return alive
    
    elif choix == "D":
        plateau[pLigne][pColonne] = "D"

        printInterface(plateau)

        cpDrapeau += 1

        if cpDrapeau == 10 :
            alive = verifWin()
            return alive
        else : return alive
    else : play()

def verifWin():
    cpMineVerif = 0
    for vligne in range(len(grille)):
        for vcolonne in range(len(grille[ligne])):
            if plateau[vligne][vcolonne] == "D" and grille[vligne][vcolonne] == "M":
                cpMineVerif += 1
    
    if cpMineVerif == cpDrapeau :
        return 2




firstmouve(plateau, grille, mine)
while alive == 0:
    play()
if alive == 1 :
    print("Vous avez perdu")
else : print("Vous avez gagner GG")