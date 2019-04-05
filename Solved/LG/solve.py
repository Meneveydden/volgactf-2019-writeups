#!/usr/bin/env python3
from functools import reduce
from math import gcd
import socket
import gmpy2

# LCG solver
# https://tailcall.net/blog/cracking-randomness-lcgs/

# m = modulus
# a = multiplier
# c = increment
# x = seed (previous value)
# states = array of lcg generated values

# Generate next value
def lcg(m, a, c, x=0):
    return (a * x + c) % m

# Generate previous value
def rlcg(m, a, c, x=0):
    ainv = gmpy2.invert(a, m)
    return ainv * (x - c) % m

# Solve for unknown increment, given modulus and multiplier
def solve_c(states, m, a):
    lcg0 = states[0]
    lcg1 = states[1]
    c = (lcg1 - a * lcg0) % m
    return c

# Solve for unknown multiplier, given modulus
def solve_a(states, m):
    lcg0 = states[0]
    lcg1 = states[1]
    lcg2 = states[2]
    a = (lcg2 - lcg1) * gmpy2.invert(lcg1 - lcg0, m) % m
    return a

# Solve for unknown modulus
def solve_m(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return modulus



if __name__ == '__main__':
    s = socket.socket()
    s.connect(('lg.q.2019.volgactf.ru', 8801))

    states = []
    while True:
        data = s.recv(40960).decode()
        if not data:
            break

        print("Received:", data)

        if 'Try this:' in data:
            for line in data.splitlines():
                if line.isdigit():
                    states.append(int(line))
            print("## states:", states)

        if 'Predict next one!' in data:
            m = solve_m(states)
            a = solve_a(states, m)
            c = solve_c(states, m, a)
            x = states[-1]
            num = lcg(m, a, c, x)
            s.send(str(num).encode() + b'\n')

        if 'VolgaCTF{' in data:
            quit()
