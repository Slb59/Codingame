"""
Le binaire avec des 0 et des 1 c'est bien. Mais le binaire avec que des 0, ou presque, c'est encore mieux.

Ecrivez un programme qui, à partir d'un message en entrée, affiche le message codé avec cette technique en sortie.

 	Règles
Voici le principe d'encodage :

Le message en entrée est constitué de caractères ASCII (7 bits)
Le message encodé en sortie est constitué de blocs de 0
Un bloc est séparé d'un autre bloc par un espace
Deux blocs consécutifs servent à produire une série de bits de même valeur (que des 1 ou que des 0) :
- Premier bloc : il vaut toujours 0 ou 00. S'il vaut 0 la série contient des 1, sinon elle contient des 0
- Deuxième bloc : le nombre de 0 dans ce bloc correspond au nombre de bits dans la série
 	Exemple
Prenons un exemple simple avec un message constitué d'un seul caractère : C majuscule. C en
binaire vaut 1000011 ce qui donne avec cette technique :

0 0 (la première série composée d'un seul 1)
00 0000 (la deuxième série composée de quatre 0)
0 00 (la troisième série composée de deux 1)
C vaut donc : 0 0 00 0000 0 00


Deuxième exemple, nous voulons encoder le message CC (soit les 14 bits 10000111000011) :

0 0 (un seul 1)
00 0000 (quatre 0)
0 000 (trois 1)
00 0000 (quatre 0)
0 00 (deux 1)
CC vaut donc : 0 0 00 0000 0 000 00 0000 0 00

 	Entrées du jeu
Entrée
Ligne 1 : le message composé de N caractères ASCII (sans retour chariot)
Sortie
Le message encodé
Contraintes
0 < N < 100
"""

import sys
import math
import numpy as np
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# message_binaire = ''.join(format(ord(i), 'b') for i in message)

message_binaire = ''.join([np.base_repr(ord(char), 2).rjust(7, '0') for char in message])
print(message_binaire)

output = ''
i = 0
j = 0
while i < len(message_binaire):

    if message_binaire[i] == '0':
        output += '00'
    else:
        output += '0'
    output += ' '
    j = i
    nb = 0
    while j < len(message_binaire) and message_binaire[j] == message_binaire[i]:
        j += 1
        nb += 1
    output += nb*'0'
    output += ' '

    i = j



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(output[:-1]+ 'c')