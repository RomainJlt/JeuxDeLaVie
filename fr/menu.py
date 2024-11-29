from config import TAILLE_MIN_GRILLE, TAILLE_MAX_GRILLE

def afficher_menu():
    print("\033[91mBienvenue dans le Jeu de la Vie!\033[0m")
    print(f"Veuillez entrer une taille de grille entre {TAILLE_MIN_GRILLE} et {TAILLE_MAX_GRILLE}.")
    print("1. Nouvelle grille")
    print("2. Charger une sauvegarde")

def demander_choix(message, choix_valides):
    while True:
        choix = input(message)
        if choix in choix_valides:
            return choix
        else:
            print(f"Entrée non valide. Veuillez entrer une des valeurs suivantes : {', '.join(choix_valides)}")
            afficher_menu()

def demander_entier(message):
    while True:
        try:
            valeur = int(input(message))
            if TAILLE_MIN_GRILLE <= valeur <= TAILLE_MAX_GRILLE:
                return valeur
            else:
                print(f"Entrée non valide. Veuillez entrer un nombre entier entre {TAILLE_MIN_GRILLE} et {TAILLE_MAX_GRILLE}.")
        except ValueError:
            print(f"Entrée non valide. Veuillez entrer un nombre entier entre {TAILLE_MIN_GRILLE} et {TAILLE_MAX_GRILLE}.")
