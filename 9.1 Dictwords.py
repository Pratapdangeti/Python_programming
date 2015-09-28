__author__ = 'pratap'


fopen = open("words.txt")

dct = {}

for line in fopen:
    words = line.rstrip().split()
    for word in words:
        if word not in dct:
            dct[word] = 1
        else:
            dct[word]+=1

print dct

print 'someone' in dct


