def findMin_1(a_list):
    min = a_list[0]
    index = 0
    for i in range(1, len(a_list)):
        if a_list[i] < min:
            min = a_list[i]
            index = i
    return index, min


print(findMin_1([8, 5, 4, 2, 3, 5, 1]))