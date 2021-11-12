# example comment
# example comment
first_name = 'Mayra'
last_name = 'Estrella'

greeting = 'Top of the morning to you,' + ' ' + first_name + ' ' + last_name + '!'

print(greeting)

# Email Generator
email = first_name[0] + '.' + last_name + '@starkindustries.com'
print(email)

# #Username Generator
username = first_name[:3] + '_' + last_name[:5]
print(username)

# # New User Contact Information
contact_card = greeting + '\n' + 'Email:' + email + '\n' + 'Username:' + username 

print(contact_card) 