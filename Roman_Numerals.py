# Write a program that prompts the user to enter a number within the range of 1 through 10.
# The program should display the Roman numeral version of that number.
# If the number is outside the range of 1 through 10, the program should display an error message.

number = int(input('Please provide a number between 1 and 10: '))

if number == 1:
    print('I')
elif number == 2:
    print('II')
elif number == 3:
    print('III')
elif number == 4:
    print('IV')
elif number == 5:
    print('V')
elif number == 6:
    print('VI')
elif number == 7:
    print('VII')
elif number == 8:
    print('VIII')
elif number == 9:
    print('IX')
elif number == 10:
    print('X')
else:
    print('That\'s not a number between 1 and 10')
