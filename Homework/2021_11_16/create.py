from main import main

# def add_items():
#     continue_or_quit = input(f'Would you like to add another item to "{grocery_list_name}? ')
#     options = ['1', '2']
#     while continue_or_quit not in options:
#         print('That is not a valid option. Please try again.')

#         if continue_or_quit == '1':
#             print()# go back to list item
#         elif continue_or_quit == '2':
#             main()

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
            main()
        elif continue_or_quit not in options:
            print('That is not a valid option. Please try again.')
        
        
        # print(groceries)
        print(one_grocery_to_rule_them_all)

    # def add_items():
    #     continue_or_quit = create() # continue_or_quit = input(f'Would you like to add another item to "{grocery_list_name}"? \n1 - Yes\n2 - No\n:')
    #     options = ['1', '2']
    #     print(continue_or_quit)
    #         # continue_or_quit = add_items()
    #         # main()
    #         # add_items()
    #         continue_or_quit = add_items()
    #     return continue_or_quit
    

    # def add_items():
        # list_items2 = input('What item would you like to have in this grocery list? ')
        # groceries[grocery_list_name] = list_items.append(list_items2)


        # if continue_or_quit == '1':
        #     print('1 successful')# go back to list item
        # elif continue_or_quit == '2':
        #     print('2 successful')
        #     # main()
        #     add_items()
        # APPEND HERE



    # I need to make it possible to insert several items in one list
    # Make a loop for inputting items unless they choose to quit OR to create a different list

# append()
    # print(groceries)


# def entries(name_entry, number_entry):
# entry = {
#     "name": "name",
#     "number": "number"
# }
# phone_book.append(entry)


# def Add_entry():
#     name_entry = input("Enter name: ")
#     number_entry = input("Enter phone number: ")
#     print(phone_book)
#     entries(name_entry,number_entry)

# print("this would add an entry")


# {'this is a list within a dictionary': ['1','2','3']}