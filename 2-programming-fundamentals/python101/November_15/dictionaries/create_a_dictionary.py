# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name: ')

# full_name = {
#     'first_name' : first_name,
#     'last_name' : last_name
# }

# print(f"My name is {full_name['last_name']}, {full_name['first_name']}")

# street address
# state
# city
# zip

# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name: ')
# company = input('Enter company name: ')
# street_name = str(input('Enter the street address: '))
# city = input('Enter the city: ')
# state = input('Enter the state: ')
# zip_code = str(input('Enter the zip code: '))

# mailing_info = {
#     'first_name' : first_name,
#     'last_name' : last_name,
#     'address': {
#         'company' : company,
#         'street_name' : street_name,
#         'state' : state,
#         'city' : city,
#         'zip_code' : zip_code}

# }

# print(f"Name:\t {mailing_info['first_name']} {mailing_info['last_name']}\nAddress: {mailing_info['address']['company']}\n\t{mailing_info['address']['street_name']}\n\t{mailing_info['address']['city']}, {mailing_info['address']['state']} {mailing_info['address']['zip_code']} ")


# customer_info = [
#     {
#         'contact_info': {
#             'Name': 'Emma Stone',
#             'Address': '12345 Oscar Rd.',
#             'Email': 'e.stone@hotmail.com'
#             },
#         'Credit Card #': '111111111111',
#         'VIP Customer': True
#     },
#     {
#         'contact_info': {
#             'Name': 'Julia Roberts',
#             'Address': '2222 Nominee Rd.',
#             'Email': 'j.roberts@hotmail.com'
#         },
#         'Credit Card #': '22222222222',
#         'VIP Customer': False
#     },
#     {
#         'contact_info': {
#             'Name': 'Lin-Manuel Miranda',
#             'Address': '56789 Tony Rd.',
#             'Email': 'lm.miranda@hotmail.com'
#         },
#         'Credit Card #': '333333333',
#         'VIP Customer': True
#     }
# ]

# # contact_card = customer_info

# for customer in customer_info:
#     print(f"\nCustomer name: {customer['contact_info']['Name']} \nCustomer address: {customer['contact_info']['Address']} \nCustomer Email: {customer['contact_info']['Email']}")

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# # # Print Elizabeth's number
# # print(phonebook_dict['Elizabeth'])

# # Add Kareem
# phonebook_dict['Kareem'] = '938-489-1234'
# # print(phonebook_dict)

# # Delete Alice
# del phonebook_dict['Alice']
# # print(phonebook_dict)

# phonebook_dict['Bob'] = '968-345-2345'
# # print(phonebook_dict)

# # Print phone entries
# for name, number in phonebook_dict.items():
#     print(name, number)

# EXERCISE 2: NESTED DICTIONARIES
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] },
#     { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] }
#   ]
# }

# # print(ramit['email'])
# # print(ramit['interests'][0])
# # print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])

# LETTER SUMMARY
# word = input('Enter a word: ')
# letter_tally = {}

# for i in word:
#     if i in letter_tally:
#         letter_tally[i] += 1
#     else:
#         letter_tally[i] = 1
# print(f'Count of letters is:\n {(letter_tally)}')

# WORD SUMMARY
sentence = input('Enter a sentence: ')
word_tally = {}
words = sentence.split()

for word in words:
    
    if word.lower() in word_tally:
        word_tally[word.lower()] += 1
    else:
        word_tally[word.lower()] = 1
print(f'Count of letters is:\n {(word_tally)}')
