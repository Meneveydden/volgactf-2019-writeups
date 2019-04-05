#!/usr/bin/env python3
import base64
import bma


def get_sequence(bin_enc_str, bin_plain_str):
    seq = []

    # get the LFSR sequence using: encrypted XOR plaintext
    for a, b in zip(bin_enc_str, bin_plain_str):
        a = int(a)
        b = int(b)
        seq.append(a ^ b)
        # print(a ^ b, end=', ')

    (poly, span) = bma.Berlekamp_Massey_algorithm(seq)
    return (poly, span, seq)

############################################################


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


if __name__ == '__main__':
    
    with open('encrypted.txt') as f:
        enc = f.read()

    hex_enc_str = base64.b64decode(enc).hex()
    bin_enc_str = bin(int(hex_enc_str, 16))[2:]

    hex_plain_str = (b'VolgaCTF{').hex()
    bin_plain_str = bin(int(hex_plain_str, 16))[2:]

    #print('bin_enc_str', bin_enc_str)
    #print('bin_plain_str', bin_plain_str)

    # get the LFSR sequence using: encrypted XOR plaintext
    # We know the flag format occurs somewhere, but not sure exactly
    # where so we bruteforce `text_offset`
    for text_offset in range(len(bin_enc_str)):
        #plaintext_offset = 0
        flag_bin_text = bin_enc_str[text_offset:]

        (poly, span, seq) = get_sequence(flag_bin_text, bin_plain_str)

        #print('poly1', poly)
        # Please note the output polynomial is using the form that its degree is always equal to the linear span.
        # For example, x^3 + x + 1 means tap positions are 0th and 1st
        poly.pop() # pop away the linear span

        # reverse tap position order
        poly = list(map(lambda i: span-i, poly))
        #print('poly2', poly)

        # the bit count / span of the register
        linear_span = span
        # original register will be our already found sequence
        # reverse due to order of the LSFR class
        register = seq[::-1] #list(reversed(seq[span:]))
        # branch of LFSR
        branches = poly

        # offset since our register is filled, so we
        # already done part of the sequence
        register_offset = len(register)

        #flag_bin_text = bin(int(binascii.hexlify(flag_text), 16))[2:]
        #print flag_bin_text
        flag_bits = [int(i) for i in flag_bin_text]
        generator = LFSR(register, branches)
        ctext = []
        for i in range(len(flag_bits)):
            next_bit = generator.next_bit()
            ctext.append(flag_bits[i] ^ next_bit)
            #assert (next_bit == seq[span+i-1])

        ciphertext = '0b' + ''.join(map(str, ctext))
        n = int(ciphertext, 2)

        # decode only if our search string is present
        if hex_plain_str not in ('%x' % n):
            continue

        if b'}'.hex() not in ('%x' % n):
            continue

        # decode
        try:
            print(bytes.fromhex('%x' % n))
        except:
            print(bytes.fromhex('0' + '%x' % n))



