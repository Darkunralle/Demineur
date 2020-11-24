import random as r

practice = [["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*","*"]]
grille = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]

#Fonction d'affichage de la grille
def printInterface(interface):
    print(interface[0])
    print(interface[1])
    print(interface[2])
    print(interface[3])
    print(interface[4])
    print(interface[5])
    print(interface[6])
    print(interface[7])
    print(interface[8])
    print(interface[9])

def printGrille(grille):
    print(grille[0])
    print(grille[1])
    print(grille[2])
    print(grille[3])
    print(grille[4])
    print(grille[5])
    print(grille[6])
    print(grille[7])
    print(grille[8])
    print(grille[9])

def firstmouve(interface):
    #print grille
    printInterface(interface)

    ligne = int(input("Entrer la ligne : "))
    colonne = int(input("Entrer la colonne : "))

    #print grille
    interface[ligne][colonne] = " "

    printInterface(interface)

    grille[ligne][colonne] = "F"
    grille[ligne][colonne-1] = "s"
    grille[ligne][colonne+1] = "s"

    grille[ligne-1][colonne] = "s"
    grille[ligne-1][colonne-1] = "s"
    grille[ligne-1][colonne+1] = "s"

    grille[ligne+1][colonne] = "s"
    grille[ligne+1][colonne-1] = "s"
    grille[ligne+1][colonne+1] = "s"



def minGen(grille):
    grille[0][r.randint(0,9)]= "X"
    grille[1][r.randint(0,9)]= "X"
    grille[2][r.randint(0,9)]= "X"
    grille[3][r.randint(0,9)]= "X"
    grille[4][r.randint(0,9)]= "X"
    grille[5][r.randint(0,9)]= "X"
    grille[6][r.randint(0,9)]= "X"
    grille[7][r.randint(0,9)]= "X"
    grille[8][r.randint(0,9)]= "X"
    grille[9][r.randint(0,9)]= "X"


def minecp(grille):
    for rows in grille:
        for row in rows :
            if row == "X":
                row = row

firstmouve(practice)
printGrille(grille)