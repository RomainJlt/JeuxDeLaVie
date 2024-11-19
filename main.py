import random 

# Demander la taille de la grille et convertir en entier
size = int(input("Entrez la taille de la grille : "))

def generate_grid(size):
    # Génère une grille de taille size x size avec des valeurs aléatoires 0 ou 1.
    return [[random.choice(["■", "."]) for _ in range(size)] for _ in range(size)]


def print_grid(grid):
    # Affiche la grille d'une manière claire et compréhensible.
    for row in grid:
        print(" ".join(str(cell) for cell in row))  # Afficher chaque cellule séparée par un espace

# Générer la grille
grid = generate_grid(size)

# Afficher la grille
print("Grille générée :")
print_grid(grid)

