__author__ = 'pratap'


fhand = raw_input("Enter file name: ")


import string
try:
    fopen = open(fhand)

except:
    print "Enter proper file name"
    exit()


dct =  {}

for line in fopen:
    line = line.strip()
    line = line.lower()
    line = line.translate(None,string.punctuation)
    line = line.translate(None,' ,0,1,2,3,4,5,6,7,8,9,\t')
    if len(line) ==0:continue
    print line
    for cht in line:
        dct[cht] = dct.get(cht,0)+1

print dct


lst = []
for key,val in dct.items():
    lst.append((val,key))

lst.sort(reverse=True)

for key,val in lst:
    print key,val


"""
5436 e
5223 a
4494 i
4174 o
4064 r
4050 t
3738 s
3123 u
3088 c
2575 n
2497 p
2436 m
2004 d
1832 l
1392 h
1257 f
1167 k
1134 b
1027 g
997 v
959 j
643 y
586 w
482 x
78 z
57 q
4

"""

