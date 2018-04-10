# define the main function
def main():
    int1 = int(input('Please enter a positive number: '))  # ask user for first positive int
    int2 = int(input('Please enter another positive number: '))  # ask user for second positive int
    print('I will run my calculations now...')

    power = power_method(int1, int2)  # establish local variable that power_method will return value to

    print(int1, 'raised by the power of', int2, 'is', power)  # print the solution to the power of problem


# define the power_method function
def power_method(x, y):  # pass the values from int1 and int2 to x and y
    if y == 1:  # if the power y(int2) is 1 return the value of x(int1)
        return x
    else:
        return x * power_method(x, y-1)  # multiple the value of x(int1) by the value of y(int1) through each recursion till 0 is reached and return the summation to the local variable power in the main function


# run the main function
main()
