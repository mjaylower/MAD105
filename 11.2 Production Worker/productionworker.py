class Employee(object):
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_wage):
        Employee.__init__(self, employee_name, employee_number)
        self.__shift_number = shift_number
        self.__hourly_wage = hourly_wage

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_wage(self, hourly_wage):
        self.__hourly_wage = hourly_wage

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_wage(self):
        return self.__hourly_wage

    def __str__(self):
        print_item = "Name: " + self.get_employee_name() + "\nID: " + str(self.get_employee_number()) + "\nShift: " + str(self.__shift_number) + "\nHourly Wage: ${:0,.2f}".format(self.__hourly_wage)
        return print_item
