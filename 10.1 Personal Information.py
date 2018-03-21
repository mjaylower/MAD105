# create the class to obtain and pass name, address, age, phone


class PersonData:
    # set the initial method for the attributes of name, address, age and phone
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # used to set a name if needing user input
    def set_name(self, name):
        self.__name = name

    # used to set an address if using user input
    def set_address(self, address):
        self.__address = address

    # used to set an age if using user input
    def set_age(self, age):
        self.__age = age

    # used to set a phone number if using user input
    def set_phone(self, phone):
        self.__phone = phone

    # gets the name passed as an argument and returns the string
    def get_name(self):
        return self.__name

    # gets the address passed as an argument and returns the string
    def get_address(self):
        return self.__address

    # gets the age passed as an argument and returns the int
    def get_age(self):
        return self.__age

    # gets the phone number passed as an argument and returns the string
    def get_phone(self):
        return self.__phone


# set the main function
def main():

    # create 3 separate instances from the class PersonData, setting the name, address, age and phone number
    person1 = PersonData('John Smith', '123 Main St. Chicago, IL', 45, '123-555-1282')
    person2 = PersonData('Jane Doe', '567 S. 2nd St. Denver, CO', 13, '555-789-8015')
    person3 = PersonData('Alexa Thomas', '3081 N. Wallace Cir. Orlando, FL', 75, '456-654-0015')

    # print the information from each instance pulled from the class PersonData get_XXX methods
    print('Person 1')
    print('--------')
    print('Name: ' + person1.get_name(),
          '\nAddress: ' + person1.get_address(),
          '\nAge:', person1.get_age(),
          '\nPhone: ' + person1.get_phone())
    print('\nPerson 2')
    print('--------')
    print('Name: ' + person2.get_name(),
          '\nAddress: ' + person2.get_address(),
          '\nAge:', person2.get_age(),
          '\nPhone: ' + person2.get_phone())
    print('\nPerson 3')
    print('--------')
    print('Name: ' + person3.get_name(),
          '\nAddress: ' + person3.get_address(),
          '\nAge:', person3.get_age(),
          '\nPhone: ' + person3.get_phone())


# run the main function
main()
