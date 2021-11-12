num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter another number: '))
count = 0

while count <= abs(num_2 - num_1):
    if (min(num_1, num_2) + count) % 2 == 1:
        print(min(num_1, num_2) + count)
    count += 1
    