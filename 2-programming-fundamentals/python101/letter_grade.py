number_grade = int(input('What was your score? '))

if number_grade < 60:
    print('F')
elif number_grade < 70:
    print('D')
elif number_grade < 80:
    print('C')
elif number_grade < 90:
    print('B')
elif 100 >= number_grade >= 90:
    print('A')
else:
    print('Error! Try again.')
