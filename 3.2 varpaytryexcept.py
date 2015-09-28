__author__ = 'pratap'


inhours = raw_input("Enter Hours: ")

try:
    hours = float(inhours)
except:
    print " Error, Please enter numeric input"
    import sys
    sys.exit()

inrate = raw_input("Enter Rate: ")

try:
    rate = float(inrate)
except:
    print "Error, please enter numeric input"
    import sys
    sys.exit()

try:
    if hours <=40:
        pay = hours*rate
        print pay

    else:
        pay = (40*rate)+((hours-40)*rate*1.5)
        print pay

except:
    print "Error, Please enter numeric input"




