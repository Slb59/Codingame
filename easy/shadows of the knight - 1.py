"""
Objectif
Vous allez rechercher les otages d'un batiment donné en sautant de fenêtre en fenêtre à l'aide de votre grappin. Votre but est d'arriver sur la fenêtre de la pièce où les otages se trouvent afin de désamorcer les bombes. Malheureusement vous n'avez qu'un nombre de sauts limités avant que les bombes n'explosent...
 	Règles
Avant chaque saut, le détecteur vous fournira la direction des bombes par rapport à votre position actuelle :
U (Up : les bombes sont situées au dessus)
UR (Up-Right : les bombes sont situées au dessus et à droite)
R (Right : les bombes sont situées à droite)
DR (Down-Right : les bombes sont situées en dessous et à droite)
D (Down : les bombes sont situées en dessous)
DL (Down-Left : les bombes sont situées en dessous et à gauche)
L (Left : les bombes sont situées à gauche)
UL (Up-Left : les bombes sont situées au dessus et à gauche)

Votre mission consiste à programmer le détecteur afin qu'il indique la position de la fenêtre sur laquelle vous devrez vous rendre au saut suivant de sorte que vous atteignez les bombes le plus tôt possible.

Les bâtiments sont représentés par des rectangles de fenêtres, la fenêtre en haut à gauche a pour position (0,0).
 	Note
Pour certains tests, la position des bombes varie d'une exécution à l'autre. L'objectif est de vous aider à trouver le meilleur algorithme possible.

Les tests fournis et les validateurs utilisés pour le calcul du score sont similaires mais différents.
 	Entrées du jeu
Le programme doit d'abord lire les données d'initialisation depuis l'entrée standard, puis, dans une boucle infinie, lire depuis l'entrée standard les données relatives à l'état courant et fournir sur la sortie standard les données demandées.
Entrées d'initialisation
Ligne 1 : 2 entiers W H. Le couple (W, H) représente la largeur et la hauteur du batiment en nombre de fenêtres.

Ligne 2 : 1 entier N, qui représente le nombre de sauts que vous pouvez faire avant que les bombes n'explosent.

Ligne 3 : 2 entiers X0 Y0, qui représentent votre position de départ.

Entrée pour un tour de jeu
La direction vers laquelle se trouve la bombe.
Sortie pour un tour de jeu
Une ligne unique avec 2 entiers X Y séparés par un espace. (X, Y) représente la position de la prochaine fenêtre sur laquelle vous devriez sauter. X représente l'index sur l'axe horizontal, Y représente l'index sur l'axe vertical. (0,0) se trouve dans le coin haut gauche du bâtiment.
Contraintes
1 ≤ W ≤ 10000
1 ≤ H ≤ 10000
2 ≤ N ≤ 100
0 ≤ X, X0 < W
0 ≤ Y, Y0 < H
Temps de réponse pour un tour ≤ 150ms
Temps de réponse pour un tour ≤ 150ms

Exemple :
10 10
6
2 5
UR
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

maxX = w
minX = 0
maxY = 0
minY = h

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if bomb_dir == "U":
        minY = y0
        y0 = (minY + maxY) / 2

    if bomb_dir == "UR":
        minX = x0
        x0 = (minX + maxX) / 2
        minY = y0
        y0 = (minY + maxY) / 2

    if bomb_dir == "R":
        minX = x0
        x0 = (minX + maxX) / 2

    if bomb_dir == "DR":
        minX = x0
        x0 = (minX + maxX) / 2
        maxY = y0
        y0 = (minY + maxY) / 2

    if bomb_dir == "D":
        maxY = y0
        y0 = (minY + maxY) / 2

    if bomb_dir == "DL":
        maxX = x0
        x0 = (minX + maxX) / 2
        maxY = y0
        y0 = (minY + maxY) / 2

    if bomb_dir == "L":
        maxX = x0
        x0 = (minX + maxX) / 2

    if bomb_dir == "UL":
        maxX = x0
        x0 = (minX + maxX) / 2
        minY = y0
        y0 = (minY + maxY) / 2

    print("%d %d" % (x0, y0))
