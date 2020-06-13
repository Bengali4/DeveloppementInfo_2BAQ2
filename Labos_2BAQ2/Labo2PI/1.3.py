import re
import sys

text = sys.argv[1]
pattern = r'(?P<Protocol>[a-z]+)\://(?P<Domain>([^/]+))(/(?P<Path>(.+)))?'
p = re.compile(pattern)
for m in p.finditer(text):
  print("Protocol : " + m.group("Protocol"))
  print("Domain : " + m.group("Domain"))
  if (m.group("Path")) is not None:
    print("Path : " + m.group("Path"))