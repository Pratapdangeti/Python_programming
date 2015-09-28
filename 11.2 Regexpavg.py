__author__ = 'pratap'



fhand = raw_input("Enter file: ")
fopen = open(fhand)


count = 0
tot = 0
import re
for line in fopen:
    x=re.findall('New Revision:.*([0-9][0-9][0-9][0-9][0-9])',line)
    if len(x)==0:continue
    a= float(x[0])
    count = count+1
    tot =tot+a

print "average of ",fhand, tot/count




