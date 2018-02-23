def main():
    number_file = open('numbers.txt', 'r')  # call the file to be read by the program

    count = 0  # set the count variable to 0 to begin checking the number of lines in the file
    average = 0  # set the average variable to be called upon later
    sum_number = 0.0  # set the accumulator

    line = number_file.readline()  # allow the file to be read
    line = line.rstrip('\n')  # remove the newline from each number in the file

    while line != '':  # while there is no a blank line, continue iterating
        number = int(line)  # convert the str from the file to an int for calculations
        line = number_file.readline()  # read the next line in the file
        line = line.rstrip('\n')  # remove the newline from the next number in the file

        sum_number += number  # add the next number to the sum_number variable for running total
        count += 1  # keep count of the number of lines read from the file to be used in average
        average = sum_number / count  # calculate the average based on lines read from file

    number_file.close()  # close the file out once the while loop has completed

    print('There are', count, 'numbers in this file.')  # print the statement displaying the number of lines read
    print('\nThe average of the numbers is:', format(average, ',.2f'))  # print the statement for the average


main()
