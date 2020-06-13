import re
patterna = r'\+[0-9]{2}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}\s[0-9]{2}'
pa = re.compile(patterna)

print(pa.match("+32 470 66 88 51"))
print(pa.match("0470 66 88 51"))

patternb = r'(-?|\+?)[1-9][0-9]*'
pb = re.compile(patternb)

print(pb.match("+19"))
print(pb.match("-8"))
print(pb.match("06"))

patternc = r'[1-9]?(([A-Z]{3}[0-9]{3})|([0-9]{3}[A-Z]{3}))'
pc = re.compile(patternc)

print(pc.match("ABC123"))
print(pc.match("1ABC123"))
print(pc.match("1123ABC"))

patternd = r'[C]\:\\'
pd = re.compile(patternd)

print(pd.match("C:\Documents"))
print(pd.match("D:\Documents"))