import re
count = 0

name = input('Enter file name:')
fh = open(name)
lines = fh.read()
match = re.findall('[0-9]+',lines)

for i in match:
	number = int(i)
	count = count + number
print (count)


    

