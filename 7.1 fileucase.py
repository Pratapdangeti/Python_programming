__author__ = 'pratap'


fopen = raw_input("Enter a file name: ")

try:
 fhand = open(fopen)

except:
 print "Please enter a valid name"
 import sys
 sys.exit()

for line in fhand:
    line = line.upper().rstrip()
    print line


