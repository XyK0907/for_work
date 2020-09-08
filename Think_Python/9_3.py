def avoids(word, avoidstr):
    for each in avoidstr:
        if each in word:
            return False
    return True


if __name__ == '__main__':
    input_str = input('请输入禁止字母字符串\n')
    fin = open('word.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if avoids(word, input_str):
            count += 1
    print(count)

