# define the main function
def main():
    n = int(input('Pick a number: '))  # allow user to enter a number to count up to
    counting(n)  # call the coutinging function


# define the counting function
def counting(n):  # pass the value from the user input int
    if n > 0:  # while the value is greater than zero execute the statements
        counting(n-1)  # set the recursive function to count down till 0 which will stop the loop
        print(n)  # print the value


# run the main function
main()
