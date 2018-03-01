def main():
    num_month = 12
    rainfall = [0] * num_month
    index = 0
    total_rainfall = 0

    print('Please enter the amount of rainfall for each month.')
    while index < num_month:
        print('Month', index + 1, ':')
        rainfall[index] = float(input())
        index += 1

    count = 0
    while count < num_month:
        total_rainfall += rainfall[count]
        count += 1

    average = total_rainfall / num_month

    print('The annual amount of rainfall is', format(total_rainfall, ',.2f'))
    print('The average monthly rainfall is', format(average, ',.2f'))
    print('The least amount of rainfall in a month was', format(min(rainfall), ',.2f'))
    print('The most amount of rainfall in a month was', format(max(rainfall), ',.2f'))


main()
