"""
	Objectif
Ghost Legs is a kind of lottery game common in Asia. It starts with a number of vertical lines. Between the lines there are random horizontal connectors binding all lines into a connected diagram, like the one below.

A  B  C
|  |  |
|--|  |
|  |--|
|  |--|
|  |  |
1  2  3

To play the game, a player chooses a line in the top and follow it downwards. When a horizontal connector is encountered, he must follow the connector to turn to another vertical line and continue downwards. Repeat this until reaching the bottom of the diagram.

In the example diagram, when you start from A, you will end up in 2. Starting from B will end up in 1. Starting from C will end up in 3. It is guaranteed that every top label will map to a unique bottom label.

Given a Ghost Legs diagram, find out which top label is connected to which bottom label. List all connected pairs.
Entrée
Line 1: Integer W and H for width and height of the diagram below.
Next H lines: Containing a Ghost Legs diagram as your input.

The diagram itself is composed of characters: '|' and '-', (and space).
The top line in the diagram has a number of labels T.
The bottom line contains labels B.

Each T and B is a single visible ASCII character that can be of any random value. Do not assume they will always be ABC or 123.

As a rule of the game, left and right horizontal connectors will never appear at the same point.

All diagrams are having the same style as the test cases.
Sortie
List all connected pairs between top and bottom labels, TB, in the order of the top labels from Left to Right. Write each pair in a separate line.
Contraintes
3 < W, H ≤ 100

ASCII characters used in the top and bottom labels are in range of Hex 21 to Hex 7E, inclusive

Entree :

7 7
A  B  C
|  |  |
|--|  |
|  |--|
|  |--|
|  |  |
1  2  3

Sortie :

A2
B1
C3
"""

import sys

def debug(a_text: str) -> None:
    print(f"Debug {a_text}", file=sys.stderr, flush=True)

map = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()
    map.append(line)

debug(map)

for alpha in map[0]:
    if alpha != ' ':
        col = map[0].index(alpha)
        for line in map[1:-1]:      
            next_col = (col+1)%w
            if line[next_col] == '-':
                col += 3
            elif line[(col-1)%w] == '-':
                col -= 3
        print(alpha + str(map[-1][col]))

