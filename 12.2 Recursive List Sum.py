def main():
    num_list = [2, 4, 6, 8, 10, 12, 14]
    list_sum = range_sum(num_list, 0, 6)
    print(list_sum)


def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)


main()
