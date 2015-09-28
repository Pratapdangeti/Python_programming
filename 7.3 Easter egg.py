
__author__ = 'pratap'

fopen = raw_input("Enter file name: ")

try:
    fhand = open(fopen)
except:
    if fopen == "na na boo boo" :
        print "na na boo boo to you - you have been punk'd !"
        import sys
        sys.exit()
    else:
        print "File cannot be opened:",fopen
        import sys
        sys.exit()

k = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        k = k+1
print "There were",k,"subject lines in",fopen
