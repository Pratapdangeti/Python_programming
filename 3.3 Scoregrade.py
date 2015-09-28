
__author__ = 'pratap'


score = raw_input("Enter Score: ")

try:
    fscore = float(score)

except:
    print("Please enter numeric ")
    import sys
    sys.exit()

if (fscore > 1.0 or fscore < 0.0) :
    print("Out of range")

elif (fscore>= 0.9):
    print("A")
elif (fscore>=0.8):
    print("B")
elif(fscore>=0.7):
    print("C")
elif (fscore>= 0.6):
    print("D")
else:
    print("F")



