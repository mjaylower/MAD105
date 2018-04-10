# def the main function
def main():
    num_list = [2, 4, 6, 8, 10, 12, 14]  # create the list to be summed
    list_sum = range_sum(num_list, 0, 6)  # select the list and range to be summed for function 'range_sum'
    print(list_sum)  # print the summation of the list 'num_list'


# def range_sum
def range_sum(num_list, start, end):  # pass the values from the list, the starting and ending values
    if start > end:  # if the start number is greater than the end, return 0
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)  # start with first values in list add to next value through ending value for each iteration/recursion


# run the main function
main()
