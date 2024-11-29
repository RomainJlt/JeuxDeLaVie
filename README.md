# JeuxDeLaVie

## Fonctionnalités
Génération de nouvelles grilles :
     -L'utilisateur peut choisir la taille de la grille entre 5 et 50 cellules.
      Chaque cellule est initialisée aléatoirement comme vivante (1) ou morte (0).


## Les règles :
Une cellule vivante reste vivante avec 2 ou 3 voisins vivants.
Une cellule morte devient vivante avec exactement 3 voisins vivants.

## Sauvegarde et reprise :
     le jeu Sauvegarde l'état actuel du jeu (grille, génération, historique).


## Menu principal
Nouvelle grille : Choisissez une taille et démarrez une partie.
Charger une sauvegarde : Reprenez une partie enregistrée précédemment.


## Commandes pour lancer le jeu
    avant de lancer le jeu il faut faire la commande suivant: "cd fr", en suite "python3 main.py" 
    Une fois le jeu lancé suivre les instruction:

## Exemple
    python3 main.py 
Bienvenue dans le Jeu de la Vie!
1. Nouvelle grille
2. Charger une sauvegarde
