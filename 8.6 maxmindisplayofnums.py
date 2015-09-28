__author__ = 'pratap'


numlst = []

while True:
    line = raw_input("Enter number: ")
    try:
        if line == "done": break
        elif int(line):
           numlst.append(line)
    except:
       print "Please enter valid number"


print "maximum value",max(numlst),",minimum value",min(numlst)


