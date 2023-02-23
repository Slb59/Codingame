"""
	Objectif
You are an intern on an Alien spacecraft, and your job is to create "Crop-Circles".

You are assigned a Farming-Field that is planted with a crop of {}
The Farming-Field is 25 high and 19 wide. The naming convention is:
The columns are a to s
The rows are a to y

The way you are told what Crop-Circle to make is notation in the format of xyd or xydd
where:
x tells you the x coordinate of the center
y tells you the y coordinate of the center
d or dd tells you the diameter (always an integer)
For example bc13 tells you center of the circle is 2nd column, 3rd row; and the diameter is 13.
NOTES:
• Some Crop-Circles will not be fully in the Farming-Field, but all centers will be.
• To be clear, a circle includes its circumference.
• There are advanced ways to determine a circle (such as Bresenham's Circle Algorithm). Do not use them; stick with what you learned in elementary school.

Mostly, Crop-Circles are made by mowing; so if no other instructions are given that's what you'll do.

However, your spacecraft is equipped with the latest technological advances in Crop-Circle creation, so you can also PLANT or PLANTMOW. Here's what that means:

PLANT = add back the {} crop to the entire circle. In other words, plant back {} as needed, so the entire area of the circle is fully planted, including spots that have already been mowed.

PLANTMOW = within a circle if a spot is planted, then mow it; if a spot is mowed, then plant it. In other words reverse it.

If you are to do either of these, the key word will be before the other part of the notation. For example: PLANTgg7 or PLANTMOWjm13

Now, go do your job, before you are transferred to the Human Probing Department or the Cattle Mutilation Division.
Entrée
A single string describing what Crop-Circles to make
Sortie
The 19-wide x 25-high Farming-Field after it has been Crop-Circled.
The only characters allowed are {} and spaces
Contraintes
There will be one or more Crop-Circles

Exemple : fg9 ls11 oe7
Sortie :
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}{}{}{}{}{}      {}{}{}
{}{}{}          {}{}{}{}          {}{}
{}{}              {}{}              {}
{}                  {}              {}
{}                  {}              {}
{}                  {}{}          {}{}
{}                  {}{}{}      {}{}{}
{}                  {}{}{}{}{}{}{}{}{}
{}{}              {}{}{}{}{}{}{}{}{}{}
{}{}{}          {}{}{}{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}{}          {}{}{}{}{}
{}{}{}{}{}{}{}{}              {}{}{}{}
{}{}{}{}{}{}{}                  {}{}{}
{}{}{}{}{}{}                      {}{}
{}{}{}{}{}{}                      {}{}
{}{}{}{}{}{}                      {}{}
{}{}{}{}{}{}                      {}{}
{}{}{}{}{}{}                      {}{}
{}{}{}{}{}{}{}                  {}{}{}
{}{}{}{}{}{}{}{}              {}{}{}{}
{}{}{}{}{}{}{}{}{}          {}{}{}{}{}
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
"""

def debug(elem:str) -> str:
    print('Debug messages' + elem)

width = 19
height = 25

occuped = '{}'
empty = '  '
plant = 'PLANT'
plantmow = 'PLANTMOW'

pos_alpha = 'abcdefghijklmnopqrstuvwxy'


field = [[1 for _ in range(width)] for _ in range(height)]

instructions = input()
instructions = instructions.split()

mode=0

for instruction in instructions:
    debug(instruction)
    if instruction.startswith(plantmow):
        mode = 2
        instruction = instruction.strip(plantmow)
    elif instruction.startswith(plant):
        mode = 1
        instruction = instruction.strip(plant)
    else:
        mode = 0
    debug(instruction)

    c = pos_alpha.index(instruction[0])
    l = pos_alpha.index(instruction[1])
    r = int(instruction[2:])**2/4
    for i in range(height):
        for j in range(width):
            d = (j-c)**2 + (i-l)**2
            if d <= r:
                if mode == 0:
                    field[i][j] = 0
                elif mode == 1:
                    field[i][j] = 1
                else:
                    field[i][j] = not field[i][j]




# ft17 PLANTft9 nf17 PLANTnf9 PLANTjm5
for i in range(height):
    line = ''
    for j in range(width):
        line += empty if field[i][j] == 0 else occuped
    print(line)
