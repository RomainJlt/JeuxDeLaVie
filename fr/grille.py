import random


# Création du module grille.py
def generer_grille(taille):
    return [[random.randint(0, 1) for _ in range(taille)] for _ in range(taille)]

def afficher_grille(grille, generation):
    # Affiche la grille dans le terminal.
    for ligne in grille:
        print(" ".join("\033[93m■\033[0m" if cellule else "." for cellule in ligne))
    print(f"Tours: {generation}")

def compter_voisins_vivants(grille, x, y):
    # Compte les voisins vivants d'une cellule.
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    taille = len(grille)
    compte = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < taille and 0 <= ny < taille and grille[nx][ny] == 1:
            compte += 1
    return compte

def prochaine_generation(grille):
    # Calcule la grille pour la génération suivante.
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
