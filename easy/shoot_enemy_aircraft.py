"""
	Objectif
There are enemy aircraft (> or <) in the sky (made of .). Each turn they move one cell forward. You are in charge of shooting them with a surface-to-air missile (^). You can only shoot vertically. Each turn your missiles move one cell up.

Note: When you shoot, the missile appears at the same altitude as the launcher. Each turn, the missile moves one cell up.

You have to print, each turn, if you WAIT or if you SHOOT. You have to shoot all the enemy aircraft, and your stock is just enough, so don't SHOOT if you can't hit an aircraft. After shooting every missile, do not print the last WAITs.
Entrée
Line 1: the number n of lines
n following lines : the description of the situation.
Sortie
As many lines as necessary, made of WAIT or SHOOT, one instruction per line.
Contraintes
2 <= n <= 10
The sky is made of n-1 lines, the last line is the ground.
A sky line is made of . if no aircraft, > or < for each aircraft.
The ground line is made of _, and ^ for the surface-to-air missile launcher.
There is only one missile launcher, and it's always on the ground.
The lengths of the lines are always the same, and <= 40.
Exemple
Entrée
6
....................
.>..................
...................<
....................
....................
_________^__________
Sortie
WAIT
WAIT
WAIT
SHOOT
WAIT
WAIT
SHOOT
"""

n = int(input())
lines=[]
nb_enemy = 0
for i in range(n):
    line = input()
    lines.append(line)
    try:
        line.find('>')
        nb_enemy +=1
    except:
        continue
    try:
        line.find('<')
        nb_enemy +=1
    except:
        continue    
craft_y = len(lines)
craft_pos = lines[-1].find('^')

while nb_enemy > 0:
    for line in lines[:craft_y]:
        if line[craft_pos] in ('>','<'):
            print('SHOOT')
            nb_enemy -= 1
        else:
            print('WAIT')
    craft_y -= 1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("WAIT")
print("SHOOT")