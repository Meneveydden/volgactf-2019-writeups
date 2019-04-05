#!/usr/bin/env python3
import base64


class LFSR:
    def __init__(self, register, branches):
        self.register = register
        self.branches = branches
        self.n = len(register)

    def next_bit(self):
        ret = self.register[self.n - 1]
        new = 0
        for i in self.branches:
            new ^= self.register[i - 1]
        self.register = [new] + self.register[:-1]

        return ret

register = [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
branches = [35, 34, 33, 32, 30, 29, 27, 25, 24, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 6, 5, 3]

register_offset = len(register)
print(offset)

with open('encrypted.txt') as f:
    enc = f.read()
hex_enc_str = base64.b64decode(enc).hex()
bin_enc_str = bin(int(hex_enc_str, 16))[2:]
flag_bin_text = bin_enc_str

#flag_bin_text = bin(int(binascii.hexlify(flag_text), 16))[2:]
#print flag_bin_text
flag_bits = [int(i) for i in flag_bin_text]
generator = LFSR(register_offset, branches)
ctext = []
for i in range(offset, len(flag_bits)):
    ctext.append(flag_bits[i] ^ generator.next_bit())

ciphertext = '0b' + ''.join(map(str, ctext))
n = int(ciphertext, 2)
print('%x' % n)
print(bytes.fromhex('%x' % n))
