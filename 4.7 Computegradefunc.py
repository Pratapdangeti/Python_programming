__author__ = 'pratap'


def computegrade(Score):
    try:
        fscore = float(Score)
    except:
        print ("Bad score")
        import sys
        sys.exit()

    if (fscore>1.0 or fscore <0.0):
        print("Out of range")
    elif (fscore > 0.9):
        print("A")
    elif(fscore>0.8):
        print("B")
    elif(fscore>0.7):
        print("C")
    elif(fscore>0.6):
        print("D")
    else:
        print("F")


computegrade(0.81)



