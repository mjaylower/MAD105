import officefurniture
import desk


def main():
    chair = officefurniture.OfficeFurniture('Chair', 'Steel', 2, 2, 50)
    desk2 = desk.Desk('Desk', 'Wood', 62, 34, 650, 'Left', 5)

    print(desk2)
    print(chair)


main()
