# import the parent class officefurniture
# import the child class desk

import officefurniture
import desk


def main():

    # using new variable pulling from the passed arguments
    chair = officefurniture.OfficeFurniture('Chair', 'Steel', 2, 2, 50)
    desk2 = desk.Desk('Desk', 'Wood', 62, 34, 650, 'Left', 5)

    # print the values passed through the classes to display the class' string
    print(desk2)
    print(chair)


# run the program
main()
