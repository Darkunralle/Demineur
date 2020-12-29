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

    cplateau = [["*"]*nbcolonne]*nbligne 

    cplateau[0][0] = 1
    print(cplateau)

    return cplateau



taille = "Practice"
plateau = creation(taille)










