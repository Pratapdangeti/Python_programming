
__author__ = 'pratap'

mx = None
mn = None

while True:
    num = raw_input("Enter number: ")
    if num == "done":
        break

    try:
        fnum = float(num)
        if mx is None or mx < fnum :
            mx = fnum
        if mn is None or mn > fnum:
            mn = fnum
    except:
        print("invalid number")

print mx,mn

