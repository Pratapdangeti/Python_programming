__author__ = 'pratap'

hours = float(raw_input("Enter hours: "))
rate = float(raw_input("Enter Rate: "))

if hours <= 40:
    pay = hours*rate
    print pay

else:
    pay = (40*rate)+((hours-40)*rate*1.5)
    print pay



