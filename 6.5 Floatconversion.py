__author__ = 'pratap'


str = 'X-DSPAM-Confidence:  0.8475'


wordidx = str.find(':')

print float(str[wordidx+1:len(str)])

