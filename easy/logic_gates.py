""" A logic gate is an electronic device implementing a boolean function, performing a logical operation on one
or more binary inputs and producing a single binary output.

Given n input signal names and their respective data, and m output signal names with their respective type of gate
and two input signal names, provide m output signal names and their respective data,
in the same order as provided in input description.

All type of gates will always have two inputs and one output.
All input signal data always have the same length.

The type of gates are :
AND : performs a logical AND operation.
OR : performs a logical OR operation.
XOR : performs a logical exclusive OR operation.
NAND : performs a logical inverted AND operation.
NOR : performs a logical inverted OR operation.
NXOR : performs a logical inverted exclusive OR operation.

Signals are represented with underscore and minus characters, an undescore matching a low level (0, or false) and
a minus matching a high level (1, or true)."""

"""
Entrée
Line 1 : n number of input signals.
Line 2 : m number of output signals.
n next lines : two space separated strings : name of input signal, then signal form.
m next lines : four space separated strings : name of output signal, then type of logic gate, 
then first input name, then second input name.
Sortie
m lines : two space separated strings : name of output signal, then signal form.
Contraintes
1 ≤ n ≤ 4
1 ≤ m ≤ 16
"""

""" Exemple :
Entrée
2
3
A __---___---___---___---___
B ____---___---___---___---_
C AND A B
D OR A B
E XOR A B

Sortie
C ____-_____-_____-_____-___
D __-----_-----_-----_-----_
E __--_--_--_--_--_--_--_--_
"""

import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())
inputs = {}
rules = []
for i in range(n):
    input_name, input_signal = input().split()
    inputs[input_name] = input_signal
for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    rules.append([output_name, _type, input_name_1, input_name_2])

for i in range(m):
    output_name, _type, input_name_1, input_name_2 = rules.pop(0)

    input_signal_1 = inputs[input_name_1]
    input_signal_2 = inputs[input_name_2]

    signal_chars = zip(input_signal_1, input_signal_2)

    output_signal = ''

    if _type == 'AND':
        for chars in signal_chars:
            output_signal += '-' if all([c == '-' for c in chars]) else '_'
    elif _type == 'OR':
        for chars in signal_chars:
            output_signal += '-' if '-' in chars else '_'
    elif _type == 'XOR':
        for l, r in signal_chars:
            output_signal += '-' if l != r else '_'
    elif _type == 'NAND':
        for chars in signal_chars:
            output_signal += '_' if all([c == '-' for c in chars]) else '-'
    elif _type == 'NOR':
        for chars in signal_chars:
            output_signal += '_' if '-' in chars else '-'
    elif _type == 'NXOR':
        for l, r in signal_chars:
            output_signal += '_' if l != r else '-'

    print(output_name + ' ' + output_signal)

