import random

def generator(strlen):
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                   'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    string_list = [letter_list[random.randrange(0, 27)] for i in range(strlen)]
    return string_list


def compare_string(random_generated, target, start):
    for i in range(start, len(target)):
        if target[i] != random_generated[i]:
            if i != start:
                print(''.join(target[0: i]))
            return i
    return len(target)


if __name__ == '__main__':
    target_string = 'methinks it is a weasel'
    target = list(target_string)
    gerated = generator(28)
    i = compare_string(gerated, target, 0)
    while i != len(target):
        gerated = generator(28)
        i = compare_string(gerated, target, i)





