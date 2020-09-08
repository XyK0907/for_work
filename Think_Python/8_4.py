def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


if __name__ == '__main__':
    print(find('mary', 'r', 1))

