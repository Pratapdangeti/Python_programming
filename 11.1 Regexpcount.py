__author__ = 'pratap'

fhand = raw_input("Enter regular expression: ")

fopen = open('mbox.txt')

import re

k = 0
for line in fopen:
    if re.findall(fhand,line):
        k = k+1

print "mbox.txt had",k,"lines that matched",fhand
