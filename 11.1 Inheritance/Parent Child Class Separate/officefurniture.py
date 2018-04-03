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
        line_item = "The " + self.__category + " is made of " + self.__material + " and is " + str(self.__length) + " by " \
                    + str(self.__width) + " and cost ${:0,.2f}" .format(self.__price)
        return line_item
