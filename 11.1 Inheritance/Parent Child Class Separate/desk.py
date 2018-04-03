import officefurniture


class Desk(officefurniture.OfficeFurniture):

    def __init__(self, category, material, length, width, price, location_of_drawers, number_drawers):

        officefurniture.OfficeFurniture.__init__(self, category, material, length, width, price)

        self.__location_of_drawers = location_of_drawers
        self.__number_drawers = number_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_drawers(self):
        return self.__number_drawers

    def __str__(self):
        print_line = "The " + self.get_category() + " is made of " + self.get_material() + " and is " + \
                     str(self.get_length()) + " by " + str(self.get_width()) + ", it has " + str(self.__number_drawers)\
                     + " on the " + self.__location_of_drawers + " and cost ${:0,.2f}".format(self.get_price())
        return print_line
