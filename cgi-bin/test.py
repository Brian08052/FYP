#!/usr/bin/python3

import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

i = int(sys.argv[1])
print(i)
print(i*2)
