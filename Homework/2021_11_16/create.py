# from main import main

one_grocery_to_rule_them_all = {}


def create():


    grocery_list_name = input('What is the name of the grocery list? ')
    list_items = input('What items would you like to have in this grocery list? ')
    groceries = []
    groceries.append(list_items)
    one_grocery_to_rule_them_all[grocery_list_name] = groceries
    # print(groceries)
    
    # groceries.append(list_items)
    # print(groceries)
    while True:
        continue_or_quit = input(f'\nWould you like to: \n1 - Add another item to "{grocery_list_name}"\n2 - Make a new grocery list \n3 - Quit\n:')
        # return continue_or_quit
        
        options = ['1', '2', '3']
        if continue_or_quit == '1':
            list_items2 = input(f'What item would you like to add to "{grocery_list_name}"? ')
            one_grocery_to_rule_them_all[grocery_list_name].append(list_items2)
            # groceries[grocery_list_name][list_items].extend(list_items2)
            
            # print(list_items)
            # print(groceries)# go back to list item
        elif continue_or_quit == '2':
            print(one_grocery_to_rule_them_all)
            create()
        elif continue_or_quit == '3':
            print(one_grocery_to_rule_them_all)
            # HOW TO GO BACK TO MENU()
            # main()
        elif continue_or_quit not in options:
            print('That is not a valid option. Please try again.')
        
        
        # print(groceries)
        print(one_grocery_to_rule_them_all)