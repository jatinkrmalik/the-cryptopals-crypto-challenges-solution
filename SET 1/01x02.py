# 2. Fixed XOR - http://cryptopals.com/sets/1/challenges/2

# Write a function that takes two equal-length buffers and produces their XOR combination.

import binascii

def XORME(x,y):
    # unhexing both the strings
    h1 = binascii.unhexlify(x)
    h2 = binascii.unhexlify(y)

    return binascii.hexlify(bytes(a ^ b for a, b in zip(h1, h2))) # XOR in Python3

x = input("Enter String 1: ")
y = input("Enter String 2: ")

print("\nXOR of String 1 and String 2: ",XORME(x,y).decode("utf-8")) # calling func w/ pretty print
