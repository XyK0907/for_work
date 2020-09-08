def has_no_e(file_name):
    fin = open(file_name)
    a = 0
    b = 0
    for line in fin:
        a += 1
        word = line.strip()
        if 'e' not in word:
            b += 1
            print(word)
    print("百分比为", round(b * 100/ a, 2), '%')


if __name__ == '__main__':
    has_no_e('word.txt')