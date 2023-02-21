"""
	Objectif
In this simplified version of "Card Counting", you are playing Blackjack at a casino table that uses only one standard deck of 52 cards.

Fortunately, you have an amazing memory and incredible math skills.
Unfortunately, you are easily distracted and there's a lot going on.

Your streamOfConsciousness is what you observe intermingled with your thoughts.
Each thought or observation (separated by a period .) might be a series of cards or something else. It is a series of cards if it consists solely of valid cards; see abbreviations used below.

With your knowledge of all the observed cards, calculate the percentageChance (rounded to the nearest whole number) that the value of the next card will be less than the bustThreshold.
(The bustThreshold is what would make your hand "go-bust"/lose by going over 21. It isn't anything you need to calculate; it is provided.)

Abbreviations used, and values:
• K = King
• Q = Queen
• J = Jack
• T = Ten
(each of the above has a value of 10)
• A = Ace (has a value of 1)
• Each number card (2 through 9, inclusive) has its own face value

Examples:
• JT7A44 means: a Jack, a Ten, a 7, an Ace, and two 4s
• JAKE might be your buddy, but it's not a series of cards, since "E" isn't a valid abbreviation
• AT&T might be your cell-service provider, but it's not a series of cards, since "&" isn't a valid abbreviation
• T1 might be a data/telecom line, but it's not a series of cards, since "1" isn't a valid abbreviation

Exemple :
222.333.444.some distraction.555.5.678.678.678.678.another distraction.9999.TTTT.JJJJ.QQQQ.KKKK.AAAA
4
Sortie : 67%
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
CARDS = ['K', 'Q', 'J', 'T', 'A']
CARDS_VALUES = [10, 10, 10, 10, 1]
values = list(range(2, 10))
percentage = [4, 4, 4, 4, 4, 4, 4, 4, 4, 16]

def value(a_card:str) -> int:
    if a_card in CARDS:
        i = CARDS.index(a_card)
        return CARDS_VALUES[i]
    else:
        return int(a_card)

stream_of_consciousness = input()
bust_threshold = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

hands = stream_of_consciousness.split('.')
memory = []
for hand in hands:
    short_memory = []
    error = False
    for c in hand:
        if c in str(values) or c in CARDS:
            short_memory.append(c)
        else:
            error = True
    if not error:
        memory.extend(short_memory)


percentageChance = 0


for card in memory:
    percentage[value(card) - 1] -= 1

nb_cards = 52 - len(memory)
nb_cards_minus = 0

for i in range(len(percentage)):
    if i < bust_threshold - 1:
        nb_cards_minus += percentage[i]

percentageChance = (nb_cards_minus/nb_cards)*100

print(str(round(percentageChance))+"%")
