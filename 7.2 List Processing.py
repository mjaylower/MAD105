import random  # import the random directory from python


def main():
    print('This program will ask the user for a number and compare it to a')
    print('list of 20 random numbers. Then it will then display which numbers')
    print('from that random list are larger than the user-entered value.')
    print('')

    rand_int = rand()  # bring in the list of random ints from the rand function
    user_number = user()  # bring in the user input number from the user function

    count = 0  # set the count to 0 - to determine if any numbers are larger than the user number
    for value in rand_int:  # for all the values in the list of random ints
        if value > user_number:  # compare the element to the user number
            print(value)
            count += 1  # if larger than user add 1 to the count
    if count == 0:  # if no numbers are larger, the count will maintain 0 - if 0, print response
        print('There are no numbers larger than yours.')


# Have a function that creates a list with 20 random integers between 1 and 100
def rand():
    n = 20  # set the number of values in the list to 20
    index = 0  # set the index to 0 to count up to 20
    rand_list = [0] * n  # create the empty list for ints multiplied by the number of values
    while index < n:  # set the while loop to determine how long the loop will run
        rand_list[index] = random.randint(1, 100)  # creates the random int for each iteration
        index += 1  # add 1 to the existing index to count up to 20 and stop running the loop
    return rand_list  # return/pass the list to a variable in the main function rand_int = rand()


# Have a function get a number from the user that is between 1 and 100
def user():
    while True:  # set the while loop to continue asking for a number until a valid entry
        try:  # use the try to eliminate terminal errors
            user_number = int(input('Pick a number between 1 and 100: '))  # ask the user for a valid number
        except ValueError:  # create an exception for anything enter that is not numeral
            print("That's not a number silly!")
        else:  # if a number is entered, check to see if it's within the correct range
            if 1 <= user_number < 100:  # check to see if number entered within range of 1-100
                break  # if number is valid, break the exception block and skip to the return clause
            else:  # if the number is not within range, print text and 'while' loop will ask again for a number
                print('Out of range. Try again')
    return user_number  # return the user entered number as a variable to 'user_number = user()' in the main function


#  run the main function
main()
