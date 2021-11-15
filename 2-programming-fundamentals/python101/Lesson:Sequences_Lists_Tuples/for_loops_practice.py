# numbers = [1, 2, 3, 4, -5, -6, -7, -8]

# Print positive numbers.
# for num in numbers:
#     if num > 0:
#         print(num)


# Print negative numbers.
# for num in numbers:
#     if num < 0:
#         print(num)


# Create a list of positive numbers.
# positive_numbers = []

# for num in numbers:
#     if num > 0:
#         positive_numbers.append(num)

# print(positive_numbers)


# Multiply a list.
# factor = 2
# product_list = []

# for num in numbers:
#     product = num * factor
#     product_list.append(product)
# print(product_list)


# Reverse a string.
# print(numbers[::-1])

# MEDIUM EXERCISES
# ????????????????
# my_list = [8, 'dalton', 4, 'emma', 2, 2, 8, 8, 'cooper']

# new_list = []

# new_list.append(set(my_list))
# print(new_list) 

# for num in my_list:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)


# my_str = 'hello my name is mayra and i like wings yay.'
# translation = ''

# for letter in my_str:
#     letter = letter.upper()
#     if  letter == 'A':
#         translation += '4'
#     elif letter == 'E':
#         translation += '3'
#     elif letter == 'G':
#         translation += '6'
#     elif letter == 'I':
#         translation += '1'
#     elif letter == 'O':
#         translation += '0'
#     elif letter == 'S':
#         translation += '5'
#     elif letter == 'T':
#         translation += '7'
#     else:
#         translation += letter.lower()
# print(translation)
    
# Long-long vowels

# my_string = 'Emma is Cooper\'s mom'
# new_string = ''
# my_string = list(my_string)

# for i in range(len(my_string)-1):
#     if my_string[i] == 'a':
#         if my_string[i] == my_string[i + 1]:
#             new_string += my_string[i] * 4
# NEED TO RENAME
#     elif i == 'e':
#         if my_string[i] == my_string[i + 1]:
#             new_string += my_string[i] * 4
#     elif i == 'i':
#         if my_string[i] == my_string[i + 1]:
#             new_string += my_string[i] * 4
#     elif my_string[i] == 'o':
#         if my_string[i] == my_string[i + 1]:
#             new_string += my_string[i] * 4
#     elif i == 'u':
#         if my_string[i] == my_string[i + 1]:
#             new_string += my_string[i] * 4
#     else:
#         new_string += my_string[i]

# # print(new_string)



# print(my_string)   
# print(new_string)


my_string = 'Emma is Cooper\'s mom'
new_string = ''
vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(len(my_string)):
    if my_string[i] in vowels:
        if my_string[i] == my_string[i + 1]:
            new_string += my_string[i] * 4
        else:
            new_string+= my_string[i]
    else:
        new_string += my_string[i]

print(new_string)

# Last letter is being left out. How do I make sure it prints? 


