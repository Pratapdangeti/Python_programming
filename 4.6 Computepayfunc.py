__author__ = 'pratap'




def pay(inhours,inrate):

 try:
     hours = float(inhours)
 except:
     print("Please enter numeric hours")
     import sys
     sys.exit()
 try:
     rate = float(inrate)
 except:
     print("Please enter numeric rate")
     import sys
     sys.exit()

 if hours <= 40:
     return hours*rate
 else:
     return 40*rate+(hours-40)*rate*1.5



x= pay(10,3)

print x


