# Write a program that asks the user for a number in the range of 1 through 7.
# The program should display the corresponding day of the week, where
# 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.
# The program should display an error message if the user enters a number that is outside the range of 1 through 7.

day_of_week = int(input('Please give me a number between 1 and 7: '))

if day_of_week == 1:
    print('Monday')
elif day_of_week == 2:
    print('Tuesday')
elif day_of_week == 3:
    print('Wednesday')
elif day_of_week == 4:
    print('Thursday')
elif day_of_week == 5:
    print('Friday')
elif day_of_week == 6:
    print('Saturday')
elif day_of_week == 7:
    print('Sunday')
else:
    print('That is not a number between 1 and 7!')
