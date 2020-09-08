def sum_lsit(num_list):
    result = []
    for i in range(1, len(num_list) + 1):
        result.append(sum(num_list[:i]))
    print(result)


sum_lsit([1, 2, 3, 4])