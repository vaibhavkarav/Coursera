# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
l3 = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    l = line.find('0')
    l1 = line[l:]
    l2 = float(l1)
    l3 = l3+l2
    count = count+1
    avg = l3/count
print("Average spam confidence:",avg)


