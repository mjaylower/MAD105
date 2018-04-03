# create the parent class for overall office furniture
# create the values used to define the object and set variables


class OfficeFurniture(object):
    def __init__(self, category, material, length, width, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__price = price

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_price(self, price):
        self.__price = price

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_price(self):
        return self.__price

# establish a string that will print with the values given for each variable
# create strings where int are used and format price for currency

    def __str__(self):
        line_item = "The " + self.__category + " is made of " + self.__material + " and is " + str(self.__length)\
                    + " by " + str(self.__width) + " and cost ${:0,.2f}" .format(self.__price)
        return line_item

# create the subclass/child class passing arguments from the OfficeFurniture class
# reestablish the init with the previously passed values as well as the class specific values
# define and create variable for local class, since parent values are hidden


class Desk(OfficeFurniture):

    def __init__(self, category, material, length, width, price, location_of_drawers, number_drawers):

        OfficeFurniture.__init__(self, category, material, length, width, price)

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

# create string that will display when child class is called upon

    def __str__(self):
        print_line = "The " + self.get_category() + " is made of " + self.get_material() + " and is " + \
                     str(self.get_length()) + " by " + str(self.get_width()) + ", it has " + str(self.__number_drawers)\
                     + " on the " + self.__location_of_drawers + " and cost ${:0,.2f}".format(self.get_price())
        return print_line
