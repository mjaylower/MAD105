# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate 12 times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall,
# and the average rainfall per month for the entire period.

print("We're going to calculate the average rainfall over a period of years...")
total_years = int(input('How many years would you like to calculate? '))
total_rainfall = 0.0

for years in range(total_years):  # ask user for how many years to record dat

    for months in range(1, 13):

        print('Year', years + 1, '- Month', months)  # for each iteration, print both year and month in question
        monthly_rainfall = float(input("How many inches of rainfall? "))  # ask user for amount of rain in given year/month

        total_rainfall += monthly_rainfall

print('Total Months:', total_years * 12)
print('Total rainfall:', total_rainfall)
print('Average Rain Per Month:', format(total_rainfall / (total_years * 12), '.1f'))
