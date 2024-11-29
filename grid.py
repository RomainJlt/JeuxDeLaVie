import random

# Définir les limites de taille
MIN_GRID_SIZE = 5
MAX_GRID_SIZE = 50

def generate_grid(size):
    # Vérifie que la taille est dans les limites définies
    if size < MIN_GRID_SIZE or size > MAX_GRID_SIZE:
        raise ValueError(f"La taille de la grille doit être entre {MIN_GRID_SIZE} et {MAX_GRID_SIZE}.")
    return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

def display_grid(grid, generation):
    for row in grid:
        print(" ".join("■" if cell else "." for cell in row))
    print(f"Génération: {generation}")