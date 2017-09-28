fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox-short.txt'
fh = open(fname)
spamcount = 0
spamtotal = 0
Confavg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    spamcount = spamcount + 1
    num = float(line[19:].rstrip())
    spamtotal = num + spamtotal
Confavg = spamtotal / spamcount
print "Average spam confidence:", Confavg