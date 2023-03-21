"""
    Objectif
Good ol' Master Mason wants to build a wall. He's got N bricks lying on the floor, each of them with different weights. The height of the bricks is 6.5 cm.

The wall is built from the bottom; in every row can be no more bricks than in the row below it. Bricks can be put right on top, if the previous condition is satisfied. In every row there’s a place for maximum X bricks.

Master Mason wants to minimize his work. Remembering old school days and physics lessons, he calculates the work as follows. If a brick is built into the L-th row from the floor, the work needed to place this brick is: W = ((L-1) * 6.5 / 100) * g * m, where m is the weight of the brick measured in kilograms and g = 10 m/s² is the (not too precise value of the) gravitational acceleration. (L-1) * 6.5 / 100 measures the distance the brick needs to be lift in meters. Note that the most bottom row ist the 1st one.

The task is to calculate the minimal work Master Mason can build all the bricks into a (not necessarily rectangular) wall.
Entrée
Line 1: An integer X for the number of bricks in a row.
Line 2: An integer N for the number of bricks.
Line 3: The integer weights of the bricks separated by space. Weights are given in kg.
Sortie
Line 1 : The minimum work. Printed exactly with 3 decimal places.
Contraintes
2 ≤ X ≤ 100
2 ≤ N ≤ 1000
0 < m < 1000
Exemple
Entrée
2
3
100 10 150
Sortie
6.500
"""


x = 2
n = 3
tabm = [100,10,150]
BRICK_HEIGH = 6.5
G = 10 # gravity in m/s

def work(level:int, m:int) -> float:
    return ((level-1) * BRICK_HEIGH / 100) * G * m

level=1
nbbrick_inlevel = 0
minw=0
tabm = sorted(tabm)[::-1]

for brick_index in range(len(tabm)):
    if nbbrick_inlevel < x:
        nbbrick_inlevel += 1
        minw += work(level, tabm[brick_index]) 
    else:
        level += 1
        nbbrick_inlevel = 1
        minw += work(level, tabm[brick_index]) 

print(f"{minw:.3f}")