from battleSystem import battle
import random
import monsters


def grassField():
    half = random.randint(0, 2)
    if half == 1:
        battle(monsters.slime)
    elif half == 2:
        battle(monsters.skeleton)
