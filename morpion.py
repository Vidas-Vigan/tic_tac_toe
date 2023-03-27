#  Créaction du tableau
tableaux = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

#  Créaction des  composant du jeux
joueuractuel = "X"
gagnant = joueuractuel
jeuxencours = True
stope_game = False

# Créaction du tableauxdu jeux
def print_tabl():
    print(tableaux[0] + " | " + tableaux[1] + " | " + tableaux[2])
    print("----------")
    print(tableaux[3] + " | " + tableaux[4] + " | " + tableaux[5])
    print("----------")
    print(tableaux[6] + " | " + tableaux[7] + " | " + tableaux[8])

# Ce que doit entrer l'utilisateur
def playerinput():
    inp = int(input("Veuillez entrer un nombre de 1-9: "))
    if inp >= 1 and inp <=9 and tableaux[inp-1] == "-":
        tableaux[inp-1] = joueuractuel
    else:
        print("Un joueur est déja en position ici!")

# Verifier Gagnant horizontale
def verif_horizontale():
    global gagnant
    if tableaux[0] == tableaux[1] == tableaux[2] and tableaux[1] != "-":
        gagnant = tableaux[0]
        return True
    elif tableaux[3] == tableaux[4] == tableaux[5] and tableaux[3] != "-":
        gagnant = tableaux[3]
        return True
    elif tableaux[6] == tableaux[7] == tableaux[8] and tableaux[6] != "-":
        gagnant = tableaux[6]
    return True


# Verifier gagant diagonale
def verif_diagonale():
    global gagnant
    if tableaux[0] == tableaux[4] == tableaux[8] and tableaux[0] != "-":
        gagnant = tableaux[0]
        return True
    elif tableaux[2] == tableaux[4] == tableaux[6] and tableaux[2] != "-":
        gagnant = tableaux[2]
        return True
    
# Verifier gagnant verticale
def verif_verticale():
    global gagnant
    if tableaux[0] == tableaux[3] == tableaux[6] and tableaux[0] != "-":
        gagnant = tableaux[0]
        return True
    elif tableaux[1] == tableaux[4] == tableaux[7] and tableaux[1] != "-":
        gagnant = tableaux[1]
        return True
    elif tableaux[2] == tableaux[5] == tableaux[8] and tableaux[0] != "-":
        gagnant = tableaux[2]
        return True

#  Vérifier si n'a plus aucun tour a jouer  
def egalite():
    if "-" not in tableaux:
        print_tabl()
        print("égalité") 

# Verifier s'il a un gagnant
def verif_victoire():
    global jeuxencours
    global stope_game
    global gagnant
    



#Echanger de jouer 

def change_jouer():
    global joueuractuel
    if joueuractuel == "X":
        joueuractuel = "O"
    else:
        joueuractuel = "X"


jeuxencours = True
stope_game = False

#  Après avoir créer les éléments créons le jeu
def tic_tac_toe():
    nb_jouer = input("Combien de jouer êtes vous?:")
    if nb_jouer == "2":
        while jeuxencours == True:
            print_tabl()
            playerinput()
            verif_horizontale()
            verif_diagonale()
            verif_verticale()
            verif_victoire()
            egalite()
            change_jouer()
        else: 
            stope_game == False
            verif_horizontale()
            verif_diagonale()
            verif_verticale()
            verif_victoire()
            egalite()
tic_tac_toe()
        