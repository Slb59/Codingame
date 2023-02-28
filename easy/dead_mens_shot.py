"""
Objectif
Captain Jack Sparrow and his pirate friends have been drinking one night. After plenty of rum, they got into an argument about who is the best shot. Captain Jack takes up some paint and paints a target on a nearby wall. The pirates take out their guns and start shooting.

Your task is to help the drunk pirates find out which shots hit the target.

Captain Jack Sparrow drew the target by drawing N lines. The lines form a convex shape defined by N corners. A convex shape has all internal angles less than 180 degrees. For example, all internal angles in a square are 90 degrees.

A shot within the convex shape or on one of the lines is considered a hit.
Entrée
Line 1: An integer N for the number of corners.
Next N lines: Two space-separated integers x and y for the coordinates of a corner. The corners are listed in a counterclockwise manner. The target is formed by connecting the corners together with lines and connecting the last corner with the first one.
Line N+1: An integer M for the number of shots.
Next M lines: Two space-separated integers x and y for the coordinates of each shot.
Sortie
M lines with either "hit" or "miss" depending on whether the shot hit the target or not.
Contraintes
3 ≤ N ≤ 10
1 ≤ M ≤ 10
-10000 < x,y < 10000

Exemple : 
Entrée :
4
-100 -100
100 -100
100 100
-100 100
5
0 0
99 99
101 101
80 -101
0 -100
Sortie:
hit
hit
miss
miss
hit
"""

import sys

def debug(a_text: str) -> None:
    print(f"Debug {a_text}", file=sys.stderr, flush=True)

corners = []
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    corners.append((x, y))

debug(corners)

m = int(input())

for i in range(m):
    answer = True
    pos, neg = False, False
    x, y = [int(j) for j in input().split()]
    for i, corner in enumerate(corners):
        j = (i + 1) % len(corners) 
        x1, y1 = corner
        x2, y2 = corners[j]

        debug(str(i) + ' ' + str(j))
        debug(str(x1) + ' ' + str(y1))
        debug(str(x2) + ' ' + str(y2))

        d = ((x - x1) * (y2 - y1)) - (y - y1) * (x2 - x1)
        debug(str(d))
        if d > 0:
            pos = True
        else:
            neg = True
        if pos == neg:    
            answer = False
            break
    print("hit" if answer else "miss")
        

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

