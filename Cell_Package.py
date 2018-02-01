# Package A: 	For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.
# Package B: 	For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.
# Package C: 	For $69.99 per month unlimited minutes provided.

# Ask the Customer what package they have, and how many minutes they used.
package = input('Do you have cell phone plan "A", "B" or "C": ')

package_a = float(39.99)
package_b = float(59.99)
package_c = float(69.99)

if package == 'C' or package == 'c':
    print('Your total bill is $', package_c)
else:
    # If package A or B is selected, ask user for minutes used
    minutes_used = float(input('How many minutes did you use this month: '))
    if (package == 'A' or package == 'a') and minutes_used <= 450:
        print('Your total bill is $', package_a)
    elif (package == 'A' or package == 'a') and minutes_used > 450:
        print('Your total bill is $', format((((minutes_used - 450) * .45) + package_a), '.02f'))
    elif (package == 'B' or package == 'b') and minutes_used <= 900:
        print('Your total bill is $', package_b)
    elif (package == 'B' or package == 'b') and minutes_used > 900:
        print('Your total bill is $', format((((minutes_used - 900) * .40) + package_b), '.02f'))
    else:
        print('Please enter valid inputs.')
