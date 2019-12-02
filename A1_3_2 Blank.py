"""
A1_3_2 Thompson.py
Programmer: Drayzdin
"""

#Place Your Code Below

guess = 13
def hiLo_game(guess, change):
    change = guess ** 2 + guess
    return change / 7
change = hiLo_game(guess, change)
print(change)
