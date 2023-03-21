"""
Objectif
You are walking on a 6-sided die one side per step. Your initial position on this cube is described by a 3-line string such as

 1
2354
 6

where
1. the first line has one whitespace and then the number on the side in front of you
2. the second line has four numbers of the sides
a. to your left
b. that you're on
c. to your right
d. opposite you and
3. the third line has one whitespace and then the number on the side behind you.

That is, in this example, you are standing on 3, going forward takes you to 1, left to 2, right to 5 and backward to 6.

You need to follow a string commands encoding movements by the characters U, L, D, R where U is forward, L is left, D is backward and R is right.

Left and right turns and moving backward also change your orientation. That is, you will always arrive on the next side with the previous side directly behind you.

For example, with the starting position given above, if you are given commands="DLU", then first you move backward to 6, then left to 5 and finally forward to 1.
Entrée
Lines 1-3: The starting position described in 3 lines as above.
Line 4: The string commands of steps you need to perform.
Sortie
The number on the side you are on after having performed commands.
Contraintes
The string commands is at most 12 characters long.
Exemple
Entrée
 1
2354
 6
DLU
Sortie
1
"""

lines = [' 1','2354',' 6']
commands = 'DLU'

j=1
for move in commands:
    if move == 'U':
        d = lines[2][1]
        lines[2][1]=lines[1][1]
        lines[0][1]=d
    elif move == "L":
        j +=1
        if j > 3:
            j=1
    elif move == "D":
        d = lines[0][1]
        lines[0][1]=lines[1][1]
        lines[1][1]=d
    elif move == "R":
        j -= 1
        if j < 0 :
            j=0

print(lines[1][j])