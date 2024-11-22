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

def count_live_neighbors(grid, x, y):
    # Compte les voisins vivants d'une cellule.
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    size = len(grid)
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and grid[nx][ny] == "■":
            count += 1
    return count



def next_generation(grid):
    # Calcule la grille pour la génération suivante.
    size = len(grid)
    new_grid = [["."] * size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            live_neighbors = count_live_neighbors(grid, x, y)
            if grid[x][y] == "■" and live_neighbors in (2, 3):
                new_grid[x][y] = "■"
            elif grid[x][y] == "." and live_neighbors == 3:
                new_grid[x][y] = "■"
    return new_grid


# Boucle de génération de générations
generations = 10
for gen in range(generations):
    print(f"\nGénération {gen + 1} :")
    print_grid(grid)
    grid = next_generation(grid)
print("\nDernière génération :")
print_grid(grid)

import os
def clear_screen():
    """Nettoie le terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
