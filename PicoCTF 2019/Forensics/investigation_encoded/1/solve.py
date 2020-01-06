#!/usr/bin/env python3
import string
from Cryptodome.Util.number import bytes_to_long
def getVal(byte):
	idx = byte>>3
	a = idx
	idx2 = 0
	idx2 = idx2 >> 29
	idx = byte
	idx += idx2
	idx &= 7
	idx -= idx2
	b = idx
	kc = key[a]
	r=7-b
	return (kc>>r)&1
data = [8,0,0x0C,8, 0x0E, 0x14, 0x0A, 0x22, 4, 0x2C, 0x0C, 0x30, 0x0C, 0x3C, 0x0A, 0x48, 6, 0x52, 0x10, 0x58, 0x0C, 0x68, 0x0C, 0x74, 0x0A, 0x80, 8, 0x8A, 0x0E, 0x92, 0x0E, 0x0A0, 0x10, 0x0AE, 0x0A, 0x0BE, 8, 0x0C8, 6, 0x0D0, 0x0A, 0x0D6, 0x0C, 0x0E0, 0x0C, 0x0EC, 0x0E, 0x0F8, 0x10, 0x106, 0x0E, 0x116, 4, 0x124]
key = [0x0B8,0x0EA,0x8E,0x0BA,0x3A,0x88,0x0AE,0x8E,0x0E8,0x0AA,0x28,0x0BB,0x0B8,0x0EB,0x8B,0x0A8,0x0EE,0x3A,0x3B,0x0B8,0x0BB,0x0A3,0x0BA,0x0E2,0x0E8,0x0A8,0x0E2,0x0B8,0x0AB,0x8B,0x0B8,0x0EA,0x0E3,0x0AE,0x0E3,0x0BA,0x80,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tree = {}
chars = string.ascii_lowercase+' '
for i in range(0,len(data),2):
	a = data[i+1]
	b = data[i]
	c = chars[i//2]
	d = ""
	for j in range(a,a+b):
		d += str(getVal(j))
	node = tree
	for e in d[:-1]:
		if e not in node:
			node[e] = {}
		node = node[e]
	node[d[-1]] = c
text = bin(bytes_to_long(open('output','rb').read()))[2:]
node = tree
flag = ""
for digit in text:
	node = node[digit]
	if type(node) == str:
		flag += node
		node = tree
print(flag)