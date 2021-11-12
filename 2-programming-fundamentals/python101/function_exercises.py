def greeting(first_name, last_name):
    print('Top of the morning to you, ' + first_name + ' ' + last_name + '!')



def email(first_name, last_name, domain):
    print (first_name[0] + '.' + last_name + domain)



def username(first_name, last_name):
    print(first_name[:3] + "_" + last_name[:5])


def contact(first_name, last_name, domain):
    greeting(first_name, last_name)
    print("Email: ") 
    email(first_name, last_name, domain)
    print("Username: ")
    username(first_name, last_name)

contact("Elizabeth", "Bennet", "@pridenoprejudice.com")
