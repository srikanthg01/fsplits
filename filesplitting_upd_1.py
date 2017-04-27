import re

a = raw_input("Enter the file to  split:")
lines = int(raw_input("Enter the number of lines with which the file to split:"))
s = re.search(r'\.\w+$', a)
s = s.group()
g = open(a,'r')

for row, con in enumerate(g):
    row=row+1

g.close()
number=1
count=0
t=0
f = open(a,'r')

for line in f:
    count += 1
    filename = ("output" + str(number) + s)
    new = open(filename, 'ab')
    new.write(line)
    t = t + int(line)
    new.close()

    if count % lines == 0:
        number += 1
	m = open("result.txt",'ab')
	m.write('The sum of lines in file %s is %s \n' % (filename, t))
	m.close()
	t = 0
    elif count == row:
        m = open("result.txt",'ab')
        m.write('The sum of lines in file %s is %s \n' % (filename, t))
        m.close()

