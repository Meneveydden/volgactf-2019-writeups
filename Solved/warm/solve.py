#!/usr/bin/env python3
# export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin
# export PYTHONPATH=~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin/python
from z3 import *

# volgactf 2019
# warm: How fast can you sove it? nc warm.q.2019.volgactf.ru 443

array = []
for i in range(16):
    array.append(BitVec(f'array__{i}', 8))

s = Solver()

# Array constraints
variable = 0x23;

s.add((variable ^ array[0]) == 0x55)
s.add((array[0x1] ^ array[0]) == 0x4e)
s.add((array[0x2] ^ array[0x1]) == 0x1e)
s.add((array[0x3] ^ array[0x2]) == 0x15)
s.add((array[0x4] ^ array[0x3]) == 0x5e)
s.add((array[0x5] ^ array[0x4]) == 0x1c)
s.add((array[0x6] ^ array[0x5]) == 0x21)
s.add((array[0x7] ^ array[0x6]) == 0x1)
s.add((array[0x8] ^ array[0x7]) == 0x34)

s.add((array[0x9] ^ array[0x8]) == 0x7)
s.add((array[0xa] ^ array[0x9]) == 0x35)
s.add((array[0xb] ^ array[0xa]) == 0x11)
s.add((array[0xc] ^ array[0xb]) == 0x37)
s.add((array[0xd] ^ array[0xc]) == 0x3c)
s.add((array[0xe] ^ array[0xd]) == 0x72)
s.add((array[0xf] ^ array[0xe]) == 0x47)


# 8 bit constraints
'''
def addConstraintBetweenXandY(solver, item, x, y):
    solver.add(x <= item, item <= y)


for i in range(16):
    addConstraintBetweenXandY(s, array[i], 0, 255) 
'''

# decode
if s.check() != sat:
    print("No solution")
    quit()
else:
    m = s.model()

    # convert to int array
    flag = [0] * 16
    for name in m:
        value = m[name]
        index = int(str(name).split('__')[1])

        flag[index] = int(str(value))
        ch = chr(flag[index])
        print(f"{name} at {hex(index)} = {value} {ch}")

    # convert to char array or string
    flag = ''.join(list(map(lambda x: chr(x) if x else 'x', flag)))
    print('flag =', flag)
    print('flag (hex) =', flag.encode().hex())

