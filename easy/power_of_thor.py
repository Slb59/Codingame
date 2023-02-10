"""
Votre programme doit permettre à Thor de rejoindre l'éclair de puissance.

Thor évolue sur une carte de 40 cases de large et 18 cases de hauteur. Notez que les coordonnées (X et Y)
commencent en partant du haut ! Ainsi la case la plus en haut à gauche a pour coordonnées
"X=0,Y=0" et celle située le plus en bas à droite a pour coordonnées "X=39,Y=17".

Au début du programme vous recevez :
la variable lightX : la position X de l'éclair que Thor doit rejoindre.
la variable lightY : la position Y de l'éclair que Thor doit rejoindre.
la variable initialTX : la position X initiale de Thor.
la variable initialTY : la position Y initiale de Thor.
À la fin du tour de jeu, vous devez afficher la direction que Thor doit prendre parmi :

N NE E SE S SO W NW

Chaque déplacement fait bouger Thor de 1 case dans la direction choisie.

Entrées du jeu
Le programme doit d'abord lire les données d'initialisation depuis l'entrée standard, puis,
dans une boucle infinie fournir sur la sortie standard les instructions de mouvement de Thor.
Entrées d'initialisation
Ligne 1 : 4 entiers lightX lightY initialTX initialTY. (lightX, lightY) indique la position de l'éclair.
(initialTX, initialTY) indique la position initiale de Thor.
Entrée pour un tour de jeu
Ligne 1 : le nombre de déplacements restant pour permettre à Thor de rejoindre l'éclair de puissance
remainingTurns. Vous pouvez ignorer cette valeur mais vous devez la lire.
Sortie pour un tour de jeu
Une ligne unique indiquant le mouvement à effectuer : N NE E SE S SW W ou NW

Contraintes
0 ≤ lightX < 40
0 ≤ lightY < 18
0 ≤ initialTX < 40
0 ≤ initialTY < 18
Temps de réponse pour un tour ≤ 100ms

"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    dir = ''

    if initial_ty > light_y and initial_ty > 0:
        initial_ty -= 1
        dir = 'N'
    elif initial_ty < light_y and initial_ty < 17:
        initial_ty += 1
        dir = 'S'

    if initial_tx < light_x and initial_tx < 40:
        dir += 'E'
        initial_tx += 1
    elif initial_tx > light_x and initial_tx > 0:
        dir += 'W'
        initial_tx -= 1

    print(dir)
