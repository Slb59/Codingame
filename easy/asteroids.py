""" Objectif
You have been tasked with studying a region of space to detect potentially dangerous asteroids.
You are given two pictures of the night sky of dimensions W*H, taken at two different times t1 and t2.
For your convenience, asteroids have been marked with capital letters A to Z, the rest is empty space represented by a dot (.) .
Using the information contained in those two pictures, determine the position of the asteroids at t3, and output a picture of the same region of the sky.

If necessary, the final coordinates are to be rounded-down (floor).
Asteroids travel at different altitudes (with A being the closest and Z the farthest from your observation point) and therefore cannot collide with each other during their transit.
If two or more asteroids have the same final coordinates, output only the closest one.
It is guaranteed that all asteroids at t1 will still be present at t2, that no asteroids are hidden in the given pictures, and that there is only one asteroid per altitude.

NB: Because of the flooring operation, it is important that you choose a coordinate system with the origin at the top left corner and the y axis increasing in the downward direction.
Entrée
Line 1: five ints separated by a space, W H t1 t2 t3
Next H lines: a row of picture 1 and picture 2, separated by a white space.
Sortie
H lines for the state of the sky at t3
Contraintes
0<W<=H<=20
0<=t1<t2<=t3<=10000

Entree:
5 5 1 2 3
A.... .A...
..... .....
..... .....
..... .....
..... .....

Sortie:
..A..
.....
.....
.....
.....


Armageddon :
20 20 25 75 100
.................O.. G...................
.....N...........U.. ...............W....
.............L.R.... ...................C
.................... ...E................
..........Z..V.H.... ..............K.....
................X... ...........T........
.............P...... ............A.......
.............A...... .....P...FLI......N.
.Q.............T.... ....................
..................F. ........D...........
.................... ......S..Y.........M
......K............W .........B....Z.....
...............Y.... ....................
..............S..... ....V.............J.
...........JE......D .........O..........
...M................ ..X...........U.....
......B..G...C....I. ....................
.................... ....................
.................... ..Q................R
.................... .......H............

Sortie :
..................K.
....................
.......I............
.........T..........
....................
...........A........
..D.F...............
.P..................
..S.......B.........
......Y.L...........
....................
....................
....................
....................
................Z...
....................
....................
....................
....................
....................
"""
import sys, math

def debug(a_text: str) -> None:
    print(f"Debug {a_text}", file=sys.stderr, flush=True)

def position_t2(alpha:str, map: list) -> tuple:
    for posx, lig in enumerate(map):
        for posy, c in enumerate(lig):
            if c == alpha:
                return posx, posy
    return -1, -1


alphabet = 'ABCDEFGHIJKLMOPQRSTUVWXYZ.'  

first_picture = []
second_picture = []

w, h, t1, t2, t3 = [int(i) for i in input().split()]
final_state = [['.' for _ in range(w)] for _ in range(h)]
for i in range(h):
    first_picture_row, second_picture_row = input().split()
    first_picture.append(first_picture_row)
    second_picture.append(second_picture_row)

for xt1, row_p1 in enumerate(first_picture):
    for yt1, c in enumerate(row_p1):
        if c in alphabet:
            pos_t2 = position_t2(c, second_picture)
            speedx = (pos_t2[0] - xt1)/(t2-t1)
            speedy = (pos_t2[1] - yt1)/(t2-t1)

            xt3 = pos_t2[0] + ((speedx) * (t3-t2))
            xt3 = math.floor(xt3)

            yt3 = pos_t2[1] + ((speedy) * (t3-t2))
            yt3 = math.floor(yt3)

            if 0<= xt3 < w and 0<= yt3 < h and alphabet.index(final_state[xt3][yt3]) > alphabet.index(c):
                final_state[xt3][yt3] = c

debug('Final state')
for i in final_state:
    for c in i:
        print(c, end='')
    print()


    ##  ==> 90% ?