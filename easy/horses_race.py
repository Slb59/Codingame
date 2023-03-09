"""
Objectif
L’Hippodrome de Casablanca organise un nouveau type de course de chevaux : les duels. Lors d’un duel, seulement deux chevaux participent à la course. Pour que la course soit intéressante, il faut sélectionner deux chevaux qui ont une puissance similaire.

Écrivez un programme qui, à partir d’un ensemble donné de puissances, identifie les deux puissances les plus proches et affiche leur écart avec un nombre entier positif.
 	Entrées du jeu
Entrée
Ligne 1 : Le nombre N de chevaux

Les N lignes suivantes : la puissance Pi de chaque cheval. Pi est un entier.

Sortie
La différence D entre les deux puissances les plus proches. D est un entier positif.
Contraintes
1 < N < 100000
0 < Pi ≤ 10000000
Exemple
Entrée
3
5
8
9
Sortie
1

"""

import math

def mindist(pi_list, horse) -> int:
    suiv = abs(pi_list[horse] - pi_list[horse+1])
    prec = abs(pi_list[horse] - pi_list[horse-1])
    return prec if prec < suiv else suiv

n = int(input())
pi_list=[]
for i in range(n):
    pi = int(input())
    pi_list.append(pi)

min = 100000
pi_list = sorted(pi_list)
for i in range(len(pi_list)-1):
    min_dist = mindist(pi_list,i)
    if min > min_dist:
        min= min_dist
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(min)