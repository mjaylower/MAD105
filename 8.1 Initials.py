def main():
    print('This program will obtain your full name and display your initials.')  # explain what the program will do

    first_name = input('What is your first name: ')  # ask the user for their first name
    middle_name = input('What is your middle name: ')  # ask the user for their middle name
    last_name = input('What is your last name: ')  # ask the users for their last name

    first_initial = first_name[0]  # create the new variable with the first index value from the first_name variable
    middle_initial = middle_name[0]  # create the new variable with the first index value from the middle_name variable
    last_initial = last_name[0]  # create the new variable with the first index value from the last_name variable

#  concatenate and print the new initial variables with the appropriate spaces and punctuation
    print('Your initials are: ' + first_initial + '. ' + middle_initial + '. ' + last_initial + '.')


#  run the program
main()
