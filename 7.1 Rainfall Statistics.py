def main():
    num_month = 12  # set the number of months to 12, as there are 12 months in a year
    rainfall = [0] * num_month  # create the list for rainfall amounts entered to be stored
    index = 0  # set the index to 0
    total_rainfall = 0  # set the accumulator to calculate total and average

    print('Please enter the amount of rainfall for each month.')
# create a while loop that adds 1 to the index and continues to run for each of the 12 months
    while index < num_month:
        print('Month', index + 1, ':')  # print the text indicating which month number the user is on
        rainfall[index] = float(input())  # ask the user to enter the amount of rainfall for said month
        index += 1  # add 1 to the index number to create a new element in the list rainfall

    count = 0  # set the count to 0 to ensure only 12 iterations are calculated and ran
    while count < num_month:
        total_rainfall += rainfall[count]  # use indexing, add the rainfall amount to itself to get the total
        count += 1  # add 1 to the count for each iteration to ensure that each months data is calculated

# find the average by adding totals from the list rainfall divided by num_months
    average = total_rainfall / num_month

    print('The annual amount of rainfall is', format(total_rainfall, ',.2f'))
    print('The average monthly rainfall is', format(average, ',.2f'))
    print('The least amount of rainfall in a month was', format(min(rainfall), ',.2f'))
    print('The most amount of rainfall in a month was', format(max(rainfall), ',.2f'))


main()
