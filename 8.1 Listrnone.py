__author__ = 'pratap'

abclst = ["abc","def","ghi","jkl","mno","pqr"]

print abclst
def chop(t):
    del t[len(t)-1]
    del t[0]

chop(abclst)
print abclst



def middle(t):
    return t[1:len(t)-1]

print middle(abclst)

print abclst

