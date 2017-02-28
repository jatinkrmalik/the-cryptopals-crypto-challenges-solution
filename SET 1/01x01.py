# 1. Convert hex to base64 - http://cryptopals.com/sets/1/challenges/1

# Always operate on raw bytes, never on encoded strings. 
# Only use hex and base64 for pretty-printing.

import binascii
import base64

str = input("Enter your hex: ")

print("\nconvering to raw bytes...")
bin = binascii.unhexlify(str);
print("Raw data- ",bin.decode("utf-8")) # pretty print in utf-8

print()

print("\nencoding in base64...")
b64 = base64.b64encode(bin)
print("Base64 encoded - ",b64.decode("utf-8")) # pretty print in utf-8

