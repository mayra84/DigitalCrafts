name = input('What is your name? ')
food_name = input('What is the name of the food you are bringing to the picnic? ')

def picnicFun(name, food_name):
    if name[0] == food_name[0]:
        return 'You are welcome to attend the party!'
    else:
        return 'Better luck next time.'
        
picnicFun(name, food_name)