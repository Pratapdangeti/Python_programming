__author__ = 'pratap'

fhand = raw_input("Enter file name: ")

try:
    fopen = open(fhand)

except:
    print "Enter valid file name: "
    exit()

dct = {}
for line in fopen:
    if line.startswith("From "):
        words = line.split()
        time = words[5].split(":")
        hour = time[0]
        dct[hour]=dct.get(hour,0)+1

print dct

lst = []

for key,val in dct.items():
    lst.append((key,val))
lst.sort()

for key,val in lst[:]:
 print key,val


