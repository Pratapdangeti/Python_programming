__author__ = 'pratap'


fhand = raw_input("Enter file name:")
fopen = open(fhand)

abc = []
for line in fopen:
    words = line.split()
    abc = abc + words
ghi = []
for i in range(len(abc)):
    if abc[i] in ghi :continue
    else:
        ghi.append(abc[i])

ghi.sort()
print ghi

