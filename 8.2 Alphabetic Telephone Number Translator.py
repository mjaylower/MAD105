def main():

    # Explains what the program will do
    print('This program will convert alphabetic phone numbers into it\'s translated digits')
    print('Please enter the 10 character phone number as "XXX-XXX-XXXX"')

    translated_number = convert_number()  # creates a new variable from the returned value found in function 'convert_number'

    print('That telephone number translates to: ' + translated_number)  # prints the translated number - the final answer..


# function calls for the users to enter a number
# will test to ensure 12 digits are entered as requested
# if 12 digits exist, function will return value to the convert_number function for execution
def get_number():

    while True:  # initiates the loop until valid number is entered
        number_entered = input('Please enter a number: ')  # sets the variable entered by user
        if len(number_entered) == 12:  # tests the variable to ensure proper validity
            return number_entered  # if proper, returns value to next function, convert_number
        else:
            print('That number is invalid')  # informs user of invalid number, loop will reiterate


# function will obtain number from get_number function
# will run through each index to either convert letter to number or keep number as-is
# will iterate until no more indexes exist
# returns value to the main function to be printed and terminate program
def convert_number():

    number_entered = get_number()  # string obtained from the get_number function is provided a new local variable
    numbers_entered_upper = number_entered.upper()  # string is converted so all alpha char are uppercase
    print('You entered: ' + numbers_entered_upper)  # prints the new uppercase number back to the user

    converted_number = ''  # new string variable created to begin translating and appending values
    index = 0  # index set to 0 to iterate through entire string

    while index < len(numbers_entered_upper):  # loop created to only run until index exceeds length of string
        for value in numbers_entered_upper[index]:  # for each value for each index, will check for alpha characters to translate
            if value == "A" or value == "B" or value == "C":  # if A, B or C will add string '2' to end of 'converted_number' var
                converted_number += '2'
                index += 1  # adds 1 to index to iterate to next char in var
            elif value == "D" or value == "E" or value == "F":  # same as above
                converted_number += '3'
                index += 1
            elif value == "G" or value == "H" or value == "I":  # same as above
                converted_number += '4'
                index += 1
            elif value == "J" or value == "K" or value == "L":  # same as above
                converted_number += '5'
                index += 1
            elif value == "M" or value == "N" or value == "O":  # same as above
                converted_number += '6'
                index += 1
            elif value == "P" or value == "Q" or value == "R" or value == "S":  # same as above
                converted_number += '7'
                index += 1
            elif value == "T" or value == "U" or value == "V":  # same as above
                converted_number += '8'
                index += 1
            elif value == "W" or value == "X" or value == "Y" or value == "Z":  # same as above
                converted_number += '9'
                index += 1
            else:
                converted_number += value  # if no alpha char found during iteration, str value added to end of var
                index += 1

    return converted_number  # return the final string value back to main function


# runs entire program
main()
