phone_book = {"adam": "678-546-6789", "john": "890-567-4567"}
def entries(name_entry, number_entry):
    entry = {
        "name": "name",
        "number": "number"
    }
    phone_book.append(entry)

def Look_up():
    names = input("What is your name?: ")
    # for i in phone_numbers:
    if names in phone_book:
        print(phone_book[names])

def Add_entry():
    name_entry = input("Enter name: ")
    number_entry = input("Enter phone number: ")
    print(phone_book)
    entries(name_entry,number_entry)

    print("this would add an entry")


def menu():
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")    
    print("5. Quit")
    choice = input()
    if choice == "1":
        Look_up()
    elif choice == "2":
        Add_entry()