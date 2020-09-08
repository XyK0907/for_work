def uses_only(word, str):
    for each in word:
        if each not in str:
            return False
    return True

if __name__ == '__main__':
    input_str = input('请输入组成字母字符串\n')
    fin = open('word.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if uses_only(word, input_str):
            print(word)
            count += 1
    print(count)