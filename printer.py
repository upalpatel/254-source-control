#!/usr/bin/env python3
from sys import argv

fh = open(argv[1],'r')
lines = list(fh)
fh.close()

print (lines[0])
print (lines[1])
print (lines[2])
print (lines[3])
