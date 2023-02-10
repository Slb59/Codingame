"""
Back in the day, people had fun turning "recipes" into surprise images using typewriters.

Use the provided recipe to create a recognizable image.

Chunks in the recipe are separated by a space.
Each chunk will tell you either
nl meaning NewLine (aka Carriage Return)
~or~
how many of the character and what character

For example:
4z means zzzz
1{ means {
10= means ==========
5bS means \\\\\ (see Abbreviations list below)
27 means 77
123 means 333333333333
(If a chunk is composed only of numbers, the character is the last digit.)

So if part of the recipe is
2* 15sp 1x 4sQ nl
...that tells you to show
**               x''''
and then go to a new line.


Abbreviations used:
sp = space
bS = backSlash \
sQ = singleQuote '
and
nl = NewLine

Entrée
string recipe
Sortie
string (multiple lines) to show the image the recipe creates
Contraintes
5 ≤ Length of recipe ≤ 1000
There won't be any double quotes (") in the recipe
recipe will contain at least 1 nl

Exemple : 1sp 1/ 1bS 1_ 1/ 1bS nl 1( 1sp 1o 1. 1o 1sp 1) nl 1sp 1> 1sp 1^ 1sp 1< nl 2sp 3|

"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

ABBREVIATIONS = ['sp', 'bS', 'sQ']
ABBREVIATIONS_TRANSLATE = [' ','\\', "'"]

list_input = t.split()

line_output = ''
for elem in list_input:
    if elem[-2:] == 'nl':
        print(line_output)
        line_output = ''
    elif elem[-2:] in ABBREVIATIONS:
        n = int(elem[0:-2])
        c = ABBREVIATIONS_TRANSLATE[ABBREVIATIONS.index(elem[-2:])]
        line_output += n * c
    else:
        n = int(elem[0:-1])
        c = elem[-1:]
        line_output += n*c

print(line_output)
