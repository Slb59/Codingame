"""
Objectif
You are given a 1-dimensional spreadsheet. You are to resolve the formulae and give the value of all its cells.

Each input cell's content is provided as an operation with two operands arg1 and arg2.

There are 4 types of operations:
VALUE arg1 arg2: The cell's value is arg1, (arg2 is not used and will be "_" to aid parsing).
ADD arg1 arg2: The cell's value is arg1 + arg2.
SUB arg1 arg2: The cell's value is arg1 - arg2.
MULT arg1 arg2: The cell's value is arg1 × arg2.

Arguments can be of two types:
• Reference $ref: If an argument starts with a dollar sign, it is a interpreted as a reference and its
 value is equal to the value of the cell by that number ref, 0-indexed.
For example, "$0" will have the value of the result of the first cell.
Note that a cell can reference a cell after itself!

• Value val: If an argument is a pure number, its value is val.
For example: "3" will have the value 3.

There won't be any cyclic references: a cell that reference itself or a cell that references it, directly or indirectly.
Entrée
Line 1: An integer N for the number of cells.
Next N lines: operation arg1 arg2

operation is one of { VALUE, ADD, SUB, MULT }
arg1 and arg2 are either a number ("-?[0-9]+"), a reference ("\$[0-9]+") or nothing "_".
Sortie
N lines: the value of each cell, one value per line, from cell 0 to cell N
Contraintes
1 ≤ N ≤ 100
-10000 ≤ val ≤ 10000
$0 ≤ $ref ≤ $(N-1)
val ∈ ℤ
ref ∈ ℕ
There are no cyclic references.
Exemple
Entrée
2
VALUE 3 _
ADD $0 4
Sortie
3
7
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
operations = []
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    operations.append([operation, arg_1, arg_2, None])

def result_operation(operation) -> int:

    if operation[3] != None:
        return operation[3]
    else:
        value1 = lec_value(operation[1])
        value2 = lec_value(operation[2])

        if operation[0] == 'VALUE':
            result = value1
        if operation[0] == 'ADD':
            result = value1 + value2
        if operation[0] == 'SUB':
            result = value1 - value2
        if operation[0] == 'MULT':
            result = value1 * value2

        operation[3] = result
        return result

def lec_value(arg):
    if arg[0] == '$':
        return result_operation(operations[int(arg[1:])])
    elif arg[0] == '_':
        return 0
    else:
        return int(arg)

for operation in operations:

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(result_operation(operation))
