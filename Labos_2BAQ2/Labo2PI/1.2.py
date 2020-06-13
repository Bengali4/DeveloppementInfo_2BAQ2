import sys
import re
pattern = r'\d+'
p = re.compile(pattern)

with open(sys.argv[1]) as file:
    i = 0
    for line in file:
        i += 1
        for m in p.finditer(line):
            print("Line " + str(i) + " , " + str(m.group()))