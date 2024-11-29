from menu import afficher_menu, demander_choix, demander_entier
from grille import generer_grille, afficher_grille, prochaine_generation
from utils import clear_screen, sauvegarder_jeu, charger_jeu, detecter_cycle

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
