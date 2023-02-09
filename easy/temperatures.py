""" Dans cet exercice, vous devez analyser un relevé de températures pour trouver
quelle température se rapproche le plus de zéro.

Écrivez un programme qui affiche la température la plus proche de 0 parmi les données d'entrée.
Si deux nombres sont aussi proches de zéro, alors l'entier positif sera considéré comme étant
le plus proche de zéro (par exemple, si les températures sont -5 et 5, alors afficher 5).

Votre programme doit lire les données depuis l'entrée standard et écrire le résultat sur la sortie standard.

Entrée
Ligne 1 : Le nombre N de températures à analyser.

Ligne 2 : Une chaine de caractères contenant les N températures exprimées
sous la forme de nombres entiers allant de -273 à 5526

Sortie
Affichez 0 (zéro) si aucune température n'est fournie. Sinon, affichez la température la plus proche de 0

Contraintes
0 ≤ N < 10000
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

result = 5526

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if int(abs(t)) < abs(result):
        result = t
    elif int(abs(t)) == abs(result):
        result = max(t, result)

if n == 0:
    print(0)
else:
    print(result)