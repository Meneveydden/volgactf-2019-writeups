#!/usr/bin/env python3
linear_span = 35
binary_sequence = '0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1'
branches = 'x^35 + x^34 + x^33 + x^32 + x^30 + x^29 + x^27 + x^25 + x^24 + x^21 + x^20 + x^19 + x^18 + x^17 + x^16 + x^15 + x^14 + x^13 + x^12 + x^11 + x^6 + x^5 + x^3'

# remove commas
binary_sequence = binary_sequence.split(', ')
binary_sequence = binary_sequence[::-1]
# retieve first 35 linear span
binary_sequence = binary_sequence[:35]

binary_sequence = list(map(int, binary_sequence))
print('register =', binary_sequence)

# create branch list from the equation
branches = branches.replace('x^', '')
branches = branches.replace(' + ', ', ')
print('branches = [' + branches + ']')
