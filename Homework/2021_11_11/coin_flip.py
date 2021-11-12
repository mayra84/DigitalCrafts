import random
num_2 = random.randint(0,1)

def flippity_floppity(num_1):
    if num_1 % 2 == 0:
        print('You flipped a coin! \nIt is heads!')
    else:
        print('You flipped a coin! \nIt is tails!')

flippity_floppity(num_1=num_2)