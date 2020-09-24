from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)

# print(coin_flip())

'''
Write a function called series_of_flips, that has one parameter, n, which represents the number of coin flips. Return a list of the random coin flips.

['H', 'H', 'T', 'H']
'''
def series_of_flips(n):
    flips = []
    for _ in range(n):
        flips.append(coin_flip())
    return flips

# print(series_of_flips(4))

'''
Write a function called four_flip_sample_space that has no parameters. It should return a list of all possible outcomes for 4 coin flips.

[
    ['H', 'H', 'H', 'H'],
    ['H', 'H', 'H', 'T'],
    ['H', 'H', 'T', 'H']
    ...
    ['T', 'T', 'T', 'T']
]
'''
def four_flip_sample_space():
    flip = ['H', 'T']
    outcomes = []

    for f1 in flip:
        for f2 in flip:
            for f3 in flip:
                for f4 in flip:
                    outcomes.append([f1, f2, f3, f4])
    
    return outcomes


'''
What is the probability that in 4 coin flips, you get 3 heads?

A = THHH
    HTHH
    HHTH
    HHHT

S = len(outcomes)
'''

four_flips = four_flip_sample_space()

three_heads = []

for lst in four_flips:
    if lst.count('H') == 3:
        three_heads.append(lst)

# print(len(three_heads))
# print(len(four_flips))
# print(len(three_heads) / len(four_flips))



'''
Suppose you call the function series_of_flips(14). What is the probability that you 
will get all 'H' values?

What is in one coin flip, that you get a heads?
   P(H) = ?
T
H <--

In two coin flips, what is the P of getting both heads?
TT
TH
HT
HH <--
'''