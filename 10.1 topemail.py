__author__ = 'pratap'


fhand = raw_input("Enter file name: ")

try:
    fopen = open(fhand)
except:
    print "Please enter valid file name"
    exit()

dct = {}
for line in fopen:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        dct[email] = dct.get(email,0)+1
print dct

lst = []
for key,val in dct.items():
    lst.append((val,key))

lst.sort(reverse=True)

for val,key in lst[:1]:
    print key,val


