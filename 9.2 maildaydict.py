__author__ = 'pratap'



fhand = raw_input("Enter file name: ")

try:
    fopen = open(fhand)

except:
    print "Please enter proper file name"
    import sys
    sys.exit()

dct = {}
for line in fopen:
    if line.startswith("From "):
     words = line.split()
     day = words[2]
     dct[day] = dct.get(day,0)+1

print dct

