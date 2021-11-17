import random


def flip_coin():

    num = random.randint(0,1)
    if num % 2 == 0:
        print('You flipped a coin! \nIt is heads!')
    else:
        print('You flipped a coin! \nIt is tails!')

