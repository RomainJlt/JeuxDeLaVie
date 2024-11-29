import os
import pickle

# Nettoie le terminal.
def suprimer_le_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Sauvegarde le terminal quand on quitte le jeu.
def sauvegarder_jeu(grille, generation, historique, fichier="sauvegarde_jeu.pkl"):
    with open(fichier, "wb") as f:
        pickle.dump((grille, generation, historique), f)

def charger_jeu(fichier="sauvegarde_jeu.pkl"):
    # Charge une grille, le compteur de génération et l'historique depuis un fichier.
    try:
        with open(fichier, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None, 0, []

#Détection des cycles 
def detecter_cycle(grille, historique):
    grille_tuple = tuple(tuple(ligne) for ligne in grille)
    if grille_tuple in historique:
        return True, historique.index(grille_tuple)
    historique.append(grille_tuple)
    return False, -1
