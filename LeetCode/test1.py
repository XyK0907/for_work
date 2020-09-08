import sys
if __name__ == "__main__":
    matrix = [[2,11,21],[19, 10, 1],[20, 11, 1],[6, 15, 24],[18, 27, 36]]
    n = 5
    k = 3
    # # 读取第一行的n
    # line_1= sys.stdin.readline().strip()
    # [n,k] = list(map(int, line_1.split()))
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     matrix.append(values)
    # print(matrix)
    a = []
    x = 0
    for attribute in range(k):
        sum_list = []
        for thing in range(n):
            for i in range(thing + 1, n):
                sum = matrix[thing][attribute] + matrix[i][attribute]
                sum_list.append(sum)
        a.append(sum_list)
    for i in range(len(matrix[1])):
        if a[0][i] == a[1][i] == a[2][i]:
            x = x+1
    print(x)

