__author__ = 'pratap'


def count(strng,lt):
    word = strng
    count = 0
    for letter in word:
        if letter == lt:
            count = count+1
    print count

count('banana','n')

