__author__ = 'pratap'

fhand = raw_input("Enter file name: ")
fopen = open(fhand)

k=0
for line in fopen:
    if line.startswith('From '):
     k = k + 1
     words = line.split()
     print words[1]

print "There were",k,"lines in the file with From as the first word"

