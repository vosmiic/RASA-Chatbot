import random

rand = random.randint(0, 1)

def randomGenerator():
    if rand == 0:
        return "You flipped... heads!"
    if rand == 1:
        return "You flipped... tails!"
