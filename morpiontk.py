from tkinter import *
from tkinter import messagebox

# msg = messagebox.askyesno(text="")


# Definition du tableau pour le mporpion
cases = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
# True pour les(X) et False les ronds(O)
drapeau = True
#  Numero du tour de jeux
n = 1

# Creaction d'une fonction pour le curseur


def afficher(event):
    # Afficher l'entrée de la souris
    # Afficher en temps réel les coordonnées
    # de la case du clique de la souris
    global drapeau, cases, n
    ligne = (event.y-2) // 100
    colonne = (event.x-2) // 100
    # Pour les drapeaux (X) et (O)
    if (n < 10) and (cases[ligne][colonne] == 0):
        if drapeau:
            dessin.create_line(100*colonne+8, 100*ligne+8, 100 *
                               colonne+96, 100*ligne+96, width=5, fill='blue')
            dessin.create_line(100*colonne+8, 100*ligne+96,
                               100*colonne+96, 100*ligne+8, width=5, fill='blue')
            cases[ligne][colonne] = 1
            message.configure(text='Au ronds de jouer')
        else:
            dessin.create_oval(100*colonne+8, 100*ligne+8, 100 *
                               colonne+96, 100*ligne+96, width=5, outline='red')
            cases[ligne][colonne] = -1
            message.configure(text='Aux croix de jouer')

        drapeau = not (drapeau)
        if (n >= 5) and (n <= 9):
            somme = verif(cases)
            if somme == 1 or somme == -1:
                n = gagner(somme)
        elif n == 9:
            n = gagner(0)
    n += 1

#  Quand on gagne ou quand on perd ou quand on fait égalité


def gagner(a):
    if a == 1:
        message.configure(text='X a gagner')
    elif a == -1:
        message.configure(text='O a gagner')
    elif a == 0:
        message.configure(text='match nul')
    return 9

# Calculer la somme de chaque ligne/colonne/diagonale
# Et verifier l'alignement
def verif(tableau):
    Sommes = [0, 0, 0, 0, 0, 0, 0, 0]      # Nous avons 8 somme a vérifier
    # Les lignes
    Sommes[0] = sum(tableau[0])
    Sommes[1] = sum(tableau[1])
    Sommes[2] = sum(tableau[2])
    # Les colonnes
    Sommes[3] = tableau[0][0] + tableau[1][0] + tableau[2][0]
    Sommes[4] = tableau[0][1] + tableau[1][1] + tableau[2][1]
    Sommes[5] = tableau[0][2] + tableau[1][2] + tableau[2][2]
    # Les diagonales
    Sommes[6] = tableau[0][0] + tableau[1][1] + tableau[2][2]
    Sommes[7] = tableau[0][2] + tableau[1][1] + tableau[2][0]
    # Pacours des sommes
    for i in range(8):
        if Sommes[i] == 3:
            return 1
        elif Sommes[i] == 3:
            return -1
    return 0

# Réintialiser les varaibles globales qui est la (cases)


def reinsis():
    global drapeau, cases, n
    cases = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    # True pour les croix et False pour les ronds(O)
    drapeau = True
    n = 1
    message.configure(text='Aux croix de jouer')
    dessin.delete(ALL)
    lignes = []
    for i in range(4):
        lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3))
        lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3))

# Créaction graphique tkinter
fenetre = Tk()
fenetre.title("Morpion")

# Dimension du morpion
fenetre.geometry("300x300")

# Créaction des zones de texte
message = Label(fenetre, text='X de jouer')
message.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

#  Creavtion du canvas
dessin = Canvas(fenetre, bg="gold", width=3001, height=3001)
dessin.grid(row=1, column=0, padx=3, pady=3, sticky=S+W+E)

# Créaction de la grille
lignes = []

# while msg

# l'évenemnt que nous avons créer en haut
dessin.bind('<Button-1>', afficher)

# Appelle de la fonction reinsis
reinsis()
fenetre.mainloop()
