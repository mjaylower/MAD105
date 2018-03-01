# Write a program that reads the contents of the two files into two separate lists.
# The user should be able to enter a boy's name or a girl's name.
# The application should check both lists, and then display messages indicating whether
# the names were among the most popular if the name was on one of the lists or that the
# name was not on the lists of popular names.


def main():

    input_boys_names_file = open('BoyNames.txt', 'r')  # open boy's name file
    boys_names = input_boys_names_file.readlines()  # create new list with names from file
    input_boys_names_file.close()  # close out boy's name file

    index = 0  # set the index to 0, so we can proceed through the list
    while index < len(boys_names):  # while there is still information in the list, continue with loop
        boys_names[index] = boys_names[index].rstrip('\n')  # for each line, remove the \n feature
        index += 1  # proceed through the list till there is no one left

# perform the exact same steps from the boys file...

    input_girls_names_file = open('GirlNames.txt', 'r')
    girls_names = input_girls_names_file.readlines()
    input_girls_names_file.close()

    index = 0
    while index < len(girls_names):
        girls_names[index] = girls_names[index].rstrip('\n')
        index += 1
    print("Enter a name to search among a database of popular boy's and girl's names")
    name_entered = input('Name: ')  # ask the user for a name to search

# create an if/elif/else statement to determine if the name
# searched appears on either the boys list or the girls list or neither

    if name_entered in boys_names:
        print("That is a common boy's name.")
    elif name_entered in girls_names:
        print("That is a common girl's name.")
    else:
        print('That is an unusual name!')


main()
