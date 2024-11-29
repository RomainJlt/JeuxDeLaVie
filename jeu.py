import random
import os
import pickle

TAILLE_MIN_GRILLE = 5
TAILLE_MAX_GRILLE = 50

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

# --- Génération et affichage de la grille ---
def generer_grille(taille):
    return [[random.randint(0, 1) for _ in range(taille)] for _ in range(taille)]

def afficher_grille(grille, generation):
    """Affiche la grille dans le terminal."""
    for ligne in grille:
        print(" ".join("\033[93m■\033[0m" if cellule else "." for cellule in ligne))
    print(f"Tours: {generation}")

def clear_screen():
    """Nettoie le terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Logique du jeu ---
def compter_voisins_vivants(grille, x, y):
    """Compte les voisins vivants d'une cellule."""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    taille = len(grille)
    compte = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < taille and 0 <= ny < taille and grille[nx][ny] == 1:
            compte += 1
    return compte

def prochaine_generation(grille):
    """Calcule la grille pour la génération suivante."""
    taille = len(grille)
    nouvelle_grille = [[0] * taille for _ in range(taille)]
    for x in range(taille):
        for y in range(taille):
            voisins_vivants = compter_voisins_vivants(grille, x, y)
            if grille[x][y] == 1 and voisins_vivants in (2, 3):
                nouvelle_grille[x][y] = 1
            elif grille[x][y] == 0 and voisins_vivants == 3:
                nouvelle_grille[x][y] = 1
    return nouvelle_grille

# --- Détection de cycle ---
def detecter_cycle(grille, historique):
    grille_tuple = tuple(tuple(ligne) for ligne in grille)
    if grille_tuple in historique:
        return True, historique.index(grille_tuple)
    historique.append(grille_tuple)
    return False, -1

# --- Gestion de sauvegarde ---
def sauvegarder_jeu(grille, generation, historique, fichier="sauvegarde_jeu.pkl"):
    with open(fichier, "wb") as f:
        pickle.dump((grille, generation, historique), f)

def charger_jeu(fichier="sauvegarde_jeu.pkl"):
    """Charge une grille, le compteur de génération et l'historique depuis un fichier."""
    try:
        with open(fichier, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None, 0, []

# --- Fonction principale ---
def main():
    afficher_menu()
    choix = demander_choix("Choix: ", ["1", "2"])
    
    if choix == "2":
        grille, generation, historique = charger_jeu()
        if grille is None:
            print("Aucune sauvegarde trouvée. Génération d'une nouvelle grille.")
            taille_grille = demander_entier("Veuillez entrer la taille de la grille : ")
            grille = generer_grille(taille_grille)
            generation = 0
            historique = []
    else:
        taille_grille = demander_entier("Veuillez entrer la taille de la grille : ")
        grille = generer_grille(taille_grille)
        generation = 0
        historique = []

    while True:
        clear_screen()
        afficher_grille(grille, generation)
        cycle_detecte, debut_cycle = detecter_cycle(grille, historique)
        if cycle_detecte:
            print(f"Géneration trouver: {debut_cycle}")

        action = input("Appuyez sur Entrée pour continuer, Q pour quitter: ").lower()
        if action == "q":
            sauvegarder_jeu(grille, generation, historique)
            print("Partie sauvegardée. À bientôt !")
            break
        grille = prochaine_generation(grille)
        generation += 1

if __name__ == "__main__":
    main()
