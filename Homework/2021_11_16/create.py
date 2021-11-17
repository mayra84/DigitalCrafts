# from main import main




def create(one_grocery_to_rule_them_all):


    store_name = input('What is the name of the grocery list? ')
    list_items = input('What items would you like to have in this grocery list? ')
    groceries = []
    groceries.append(list_items)
    one_grocery_to_rule_them_all[store_name] = groceries
    # print(groceries)
    
    # groceries.append(list_items)
    # print(groceries)
    
    while True:
        continue_or_quit = input(f'\nWould you like to: \n1 - Add another item to "{store_name}"\n2 - Make a new grocery list \n3 - Go back to main menu\n:')
        # return continue_or_quit
        
        options = ['1', '2', '3']
        if continue_or_quit == '1':
            list_items2 = input(f'What item would you like to add to "{store_name}"? ')
            one_grocery_to_rule_them_all[store_name].append(list_items2)
            # groceries[store_name][list_items].extend(list_items2)
            
            # print(list_items)
            # print(groceries)# go back to list item
        elif continue_or_quit == '2':
            print(one_grocery_to_rule_them_all)
            create()
        elif continue_or_quit == '3':
            print(one_grocery_to_rule_them_all)
            break
            # HOW TO GO BACK TO MENU()
            # main()
        elif continue_or_quit not in options:
            print('That is not a valid option. Please try again.')
        
        
        # print(groceries)
        print(one_grocery_to_rule_them_all)

