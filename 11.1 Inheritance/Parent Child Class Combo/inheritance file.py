# import the parent/child class file

import inheritance


def main():

    # create new variable to pass values as arguments to the classes program
    chair = inheritance.OfficeFurniture('Chair', 'Steel', 2, 2, 50)
    desk2 = inheritance.Desk('Desk', 'Wood', 62, 34, 650, 'Left', 5)

    # print the string from each of the class' using the values in the variables as they are passed
    print(desk2)
    print(chair)


# run the program
main()
