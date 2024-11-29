from grid import generate_grid, display_grid
from game_logic import next_generation
from cycle_detection import detect_cycle
from save_load import save_grid, load_grid
from clear import clear_screen



from grid import generate_grid, display_grid, MIN_GRID_SIZE, MAX_GRID_SIZE

def main():
    print("Bienvenue dans le Jeu de la Vie !")
    choice = input("1. Nouvelle grille\n2. Charger une sauvegarde\nChoix : ")
    
    if choice == "2":
        grid = load_grid()
        if grid is None:
            print("Aucune sauvegarde trouvée. Génération d'une nouvelle grille.")
            size = get_grid_size()
            grid = generate_grid(size)
    else:
        size = get_grid_size()
        grid = generate_grid(size)

    history = []
    generation = 0
    while True:
        clear_screen()
        display_grid(grid, generation)
        cycle_detected, cycle_start = detect_cycle(grid, history)
        if cycle_detected:
            print(f"Cycle détecté ! Début : {cycle_start}, Longueur : {len(history) - cycle_start}")

        action = input("Appuyez sur Entrée pour continuer, Q pour quitter : ").lower()
        if action == "q":
            save_grid(grid)
            print("Partie sauvegardée. À bientôt !")
            break
        grid = next_generation(grid)
        generation += 1

def get_grid_size():
    # Demande à l'utilisateur une taille de grille valide.
    while True:
        try:
            size = int(input(f"Entrez la taille de la grille ({MIN_GRID_SIZE}-{MAX_GRID_SIZE}) : "))
            if MIN_GRID_SIZE <= size <= MAX_GRID_SIZE:
                return size
            else:
                print(f"Erreur : La taille doit être comprise entre {MIN_GRID_SIZE} et {MAX_GRID_SIZE}.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()
