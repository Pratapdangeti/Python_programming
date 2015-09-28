__author__ = 'pratap'

fopen = raw_input("Enter file name: ")

try:
    fhand = open(fopen)
except:
    if fopen == "na na boo boo" :
        print "na na boo boo to you"
        import sys
        sys.exit()
    else:
        print "Please enter valid file name"
        import sys
        sys.exit()

k = 0
tot = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        strt = line.find(':')
        conf = float(line[strt+1:len(line)])
        k = k+1
        tot = tot+conf
print "Average spam confidence: ",tot/k

