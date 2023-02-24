"""
Objectif
Your adventure path led you to an inn in a small, forgotten town somewhere to the North of Golem Hills.
After gulping the last drop from the 9th mug of elf wine a shady old man materializes out of nowhere, in-front of you.
You start to doubt the wine.
The old man (throwing a pack of old maps on the table): Do you want to earn some good coins?
You (without looking at him): I've enough for food and wine!
The old man: What about a whole inn...!
You: Hm...
The old man: Yeees and you'll get the glory of being the first one to get to this treasure!
You (looking at the bunch of maps): But they look the same!?
The old man: Or do they, you must choose wisely.
The voice of the old man (from nowhere): Ah right, one more thing, beware of the Dragons!
You grab your staff and sword, swallow one more whole mug of wine:
Well, it's glory time!

You are given N maps for a dungeon. Each map may contain a path to a treasure T,
from starting position [ startRow; startCol ]. Determine the index of the map which holds
the shortest path from the starting position to T, but be careful a map may lead you to a TRAP.

A path is marked on the map with ^, v, <, > symbols, each corresponding to UP, DOWN, LEFT, RIGHT
directions respectively, i.e. each symbol shows you the next cell to move on.

A valid path must start from [ startRow; startCol ] and end on T.

The path length is the count of direction symbols plus 1, for the T cell.

Example:
W = 4 H = 4
startRow = 1 startCol = 1
N = 3

Maps:
0
.>>v
.^#v
..#v
...T

1
....
.v#.
.v#.
.>>T

2
....
v<#.
v.#.
..>T


In the above example map 2 does not contain a valid path from [1; 1] to T, map 0
contains a valid path with length 7 (the count of the direction symbols + T) and
 map 1 contains a valid path with length 5, so the answer is 1.
Entrée
Line 1: Width W and height H of the maps
Line 2: startRow and startCol for the starting position on the map
Line 3: An integer N for the number of maps to check
N * H Lines: Each H consecutive lines are representing a single map. Each line contains W characters representing a row of a map.

Characters can be:
. - Empty square
# - Wall
^ - Move UP
v - Move DOWN
< - Move LEFT
> - Move RIGHT
T - The treasure square
Sortie
index of the map with the shortest path. If there isn't a map with valid path from [ startRow; startCol ] to T output TRAP.
Contraintes
There is always a T on the maps.
If there are maps with valid path from [ startRow; startCol ] to T only one map holds the shortest path.
The given maps are representing the same dungeon, but the position for T may differ.
0 < N < 10
2 < W, H < 20

Exemple :
4 4
1 1
3
.>>v
.^#v
..#v
...T
....
.v#.
.v#.
.>>T
....
v<#.
v.#.
..>T

Exemple :
19 12
2 4
2
###################
#.................#
#..>>>v......>T...#
#..^..>v.....^<...#
#..^...>v.........#
#..^....v....>v...#
#..^....v....^v...#
#..^...v<....^v...#
#..^..v<.....^v...#
#..^<<<......^<...#
#.................#
###################
###################
#.................#
#...>>>v......>T..#
#...^..>v.....^<..#
#...^...>v........#
#...^....v....>v..#
#...^....v....^v..#
#...^...v<....^v..#
#...^..v<.....^v..#
#...^<<<......^<..#
#.................#
###################
"""

import sys
from pprint import pprint


def debug(a_text: str) -> None:
    print(f"Debug {a_text}", file=sys.stderr, flush=True)


def valid_path(a_map: list) -> tuple:
    posrow = start_row
    poscol = start_col
    lenmap = 0

    while True:
        if lenmap > width * heigh or posrow >= heigh or poscol >= width:
            break

        c = a_map[posrow][poscol]
        lenmap += 1
        debug(posrow)
        debug(poscol)
        debug(a_map[posrow][poscol])
        debug(lenmap)

        if a_map[posrow][poscol] == '>':
            poscol += 1
        elif a_map[posrow][poscol] == 'v':
            posrow += 1
        elif a_map[posrow][poscol] == '<':
            poscol -= 1
        elif a_map[posrow][poscol] == '^':
            posrow -= 1
        else:
            break

    if lenmap > width * heigh or posrow >= heigh or poscol >= width:
        return False, -1
    elif a_map[posrow][poscol] == 'T':
        return True, lenmap
    else:
        return False, -1


width, heigh = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]
nb_maps = int(input())
maps = [[['.' for _ in range(width)] for _ in range(heigh)] for _ in
        range(nb_maps)]

for iMap in range(nb_maps):
    for iLin in range(heigh):
        map_row = input()
        for iCol, c in enumerate(map_row):
            maps[iMap][iLin][iCol] = c

min_map = -1
min_len = width * heigh
for iMap in range(nb_maps):
    valid_map, len_map = valid_path(maps[iMap])
    debug(str(iMap) + str(len_map))
    if valid_map:
        if len_map < min_len:
            min_map = iMap
            min_len = len_map

print(min_map if min_map >= 0 else 'TRAP')