fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()
for line in fh:
    if not line.startswith("From:") : continue
    l = line.rstrip().split()
    print(l[1])
    count = count+1

print("There were", count, "lines in the file with From as the first word")



