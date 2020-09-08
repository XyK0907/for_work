import random

def generator(strlen):
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                   'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    string_list = [letter_list[random.randrange(0, 27)] for i in range(strlen)]
    return ''.join(string_list)


def compare_string(random_generated, target):
    numSame = 0
    for i in range(len(target)):
        if target[i] == random_generated[i]:
            numSame += 1
    return numSame/len(target)


if __name__ == '__main__':
    target_string = 'thinks'
    gerated = generator(6)
    best_ratio = 0
    ratio = compare_string(gerated, target_string)
    i = 0
    while  ratio < 1:
        if ratio > best_ratio:
            print(ratio, gerated)
            best_ratio = ratio
        i += 1
        gerated = generator(6)
        ratio = compare_string(gerated, target_string)





