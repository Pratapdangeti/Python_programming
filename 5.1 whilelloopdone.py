
__author__ = 'pratap'



k = 0
t = 0


while True:
    num = raw_input("Enter a number: ")
    if num=="done":
        break
    try:
        fnum = float(num)
        k=k+1
        t = t+fnum
    except:
        print("invalid input")

if k==0:
 print t,k,0
else:
 print t,k,t/k


