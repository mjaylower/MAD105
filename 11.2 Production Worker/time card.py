import productionworker


def main():
    #  get the name and id for the employee
    #  creates the local variable from the parent class

    name = input('Name: ')
    id_number = input('Employee ID: ')

    #  get the shift worked and hourly wage
    #  create the local variables from the child class

    # create a loop to ensure the correct shift is entered
    shift_worked = int(input('Shift Worked: '))
    while shift_worked != 1 and shift_worked != 2:
        print('Please enter 1 for Day Shift or 2 for Night Shift')
        shift_worked = int(input('Shift Worked: '))

    wage = float(input('Hourly Wage: '))

    #  create the production worker object using local variables to pass to classes
    shift_info = productionworker.ProductionWorker(name, id_number, shift_worked, wage)

    # print the results from user input data
    # this file shows how both methods of displaying information works
    print('\n')
    print('Information from current file')
    print('-------------------------------')
    print('Name: ' + shift_info.get_employee_name())
    print('ID: ' + str(shift_info.get_employee_number()))
    print('Shift Worked: ' + str(shift_info.get_shift_number()))
    print('Hourly Wage: ${:0,.2f}'.format(shift_info.get_hourly_wage()))

    # display how information from production worker.py - line 37 - __str__ also works..
    # can comment out the items below to one display once if you wish
    print('\n')
    print('Information pulled from production worker class')
    print('---------------------------')
    print(shift_info)


# run program
main()
