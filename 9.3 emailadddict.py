__author__ = 'pratap'

fhand = raw_input("Enter a file name: ")

try:
    fopen = open(fhand)
except:
    print "Enter valid file name"

dct = {}
for line in fopen:
    if line.startswith("From "):
        words = line.split()
        eid = words[1]
        dct[eid]=dct.get(eid,0)+1


print dct


