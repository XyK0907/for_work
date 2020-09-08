if __name__ == '__main__':
    fin = open('word.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)