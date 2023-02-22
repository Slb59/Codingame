"""
Objectif
Calculate the equivalent resistance of a circuit containing only resistors.

A resistor is a component used in electrical circuits. A resistor is quantified by its Resistance, which is measured in Ohms. We are interested in knowing the total resistance of a circuit of only resistors. There are two key definitions needed to determine the resistance of multiple resistors.

1. Series

The resistance of resistors in a line is equivalent to the sum of the resistance of those resistors.

    ---[R_1]---[R_2]---

Resistors in series will be noted with parentheses ( R_1 R_2 R_3 ... and so on ).

The resistance of a series arrangement is: R_eq = R_1 + R_2 + R_3 + ... and so on, where R_eq is the equivalent resistance of the series arrangement.

2. Parallel

The resistance of resistors in branching paths of the circuit is equal to 1 over the sum of 1 over the resistance of each branching path.

       +---[R_1]---+
       |           |
    ---+           +---
       |           |
       +---[R_2]---+


Resistors in parallel will be noted with brackets [ R_1 R_2 R_3 ... and so on ].

The resistance of resistors in parallel is R_eq = 1/(1/R_1 + 1/R_2 + 1/R_3 + 1/... and so on).

A branch can be treated as a single resistor by determining its equivalent resistance.

Example:

N = 3
A 24
B 8
C 48
[ ( A B ) [ C A ] ]

This will look something like this:

       +---[C]---+
       |         |
    +--+         +--+
    |  |         |  |
    |  +---[A]---+  |
    |               |
    +---[A]---[B]---+
    |               |
    +---[Battery]---+

[ ( A B ) [ C A ] ] => [ 24+8 1/(1/48+1/24) ] => [ 32 16 ] => 1/(1/32+1/16) => 32/3 => 10.666... => 10.7
Entrée
Line 1: An integer N for the number of unique resistors present in the circuit
Next N lines: A space separated name and the integer resistance R of a resistor
Last line: A space separated combination of parentheses, brackets, and names of resistors
Sortie
The equivalent resistance expressed as a float rounded to the nearest 0.1 Ohms.
Contraintes
0 < N < 10
0 < R < 100

Entrée :
2
A 20
B 10
( A B )
Sortie : 30.0

2
C 20
D 25
[ C D ]
-> 11.1

3
A 24
B 8
C 48
[ ( A B ) [ C A ] ]
-> 10.7

7
Alfa 1
Bravo 1
Charlie 12
Delta 4
Echo 2
Foxtrot 10
Golf 8
( Alfa [ Charlie Delta ( Bravo [ Echo ( Foxtrot Golf ) ] ) ] )
-> 2.4

"""

def calc_series(rs):
    return sum([float(r) for r in rs])

def calc_parallel(rs):
    return 1 / sum([1 / float(r) for r in rs])

circuit_in_list = []

n = int(input())
resistors = {}
for i in range(n):
    inputs = input().split()
    name = inputs[0]
    r = int(inputs[1])
    resistors[name] = r
circuit = input()

for k, v in resistors.items():
    circuit = circuit.replace(k, str(v))
circuit = circuit.split()

while len(circuit) >= 2:
    last_left_part_index = max([index for index, elm in enumerate(circuit) if elm in ['[', '(']])
    pair_part_elements = circuit[last_left_part_index:]
    pair_right_part_index = min([index for index, elm in enumerate(pair_part_elements) if elm in [']', ')']])
    pair_right_part_index += last_left_part_index
    rs = circuit[last_left_part_index + 1:pair_right_part_index]
    last_left_part = circuit[last_left_part_index]
    r = calc_parallel(rs) if last_left_part == '[' else calc_series(rs)
    circuit[last_left_part_index:pair_right_part_index + 1] = [r]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print('%.1f' % r)
