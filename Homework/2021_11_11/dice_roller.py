import random
import time

def dicety_rollery(num_1):
    num_2 = random.randint(1,num_1)
    print("It's Rolling......")
    time.sleep(3)
    print(num_2)

print("Let's roll a dice!")
num_1 = int(input("How many sides should it have? (2-20):"))
dicety_rollery(num_1=num_1)