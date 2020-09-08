def is_abecedarian(word):
    word = word.lower()
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True

print(is_abecedarian('AbCA'))