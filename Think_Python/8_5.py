def count(word, letter):
    count = 0
    for each in word:
        if each == letter:
            count += 1
    print(count)


if __name__ == '__main__':
    count('happppppy', 'p')

    print('happpppppy'.count('p'))