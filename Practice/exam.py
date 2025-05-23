import random


class Coin:
# The _ _init_ _ method initializes the sideup data attribute with 'Heads'.

def__init__(self):
    self.sideup='Heads'
# The toss method generates a random number
# in the range of 0 through 1. If the number
# is 0, then sideup is set to 'Heads'.
# Otherwise, sideup is set to 'Tails'.
def toss(self):
    if random.randint(0, 1) == 0:
        self.sideup = 'Heads'
    else:
        self.sideup = 'Tails'
def get_sideup(self):
    return self.sideup