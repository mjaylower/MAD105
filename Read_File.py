def main():
    count = 0  # set the count variable to 0 to begin checking the number of lines in the file
    input_file = open('names.txt', 'r')  # call the file to be read by the program

    name = input_file.readline()  # allow the file to be read
    name = name.rstrip('\n')  # remove the newline tag so name appear sequentially

    while name != '':  # while there is no a blank line, continue iterating
        print(name)  # print the name from the file
        name = input_file.readline()
        name = name.rstrip('\n')

        count += 1  # keep count of the number of lines read from the file

    input_file.close()  # close the file out once the while loop has completed

    print('\nThere are', count, 'names in this file.')  # print the statement displaying the number of lines read


#  call the main function
main()
