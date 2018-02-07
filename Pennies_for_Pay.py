# ask for the number of days the user will work for
days_worked = int(input('How many days will you work for pennies on the dollar? '))
pay = .01
total = 0.0

# print heading
print('Days Worked', '\t', 'Amount Earned That Day')
print('-------------------------------------------')

# create a range loop with user input
for days in range(1, (days_worked + 1)):
    print(format(days, '7.0f'), '\t', '|', '\t\t', '$', pay)
    total += pay
    pay = pay * 2

# display total monies made
print('The total amount earned is: $', format(total, '.2f'))
