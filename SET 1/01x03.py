# Single-byte XOR cipher - http://cryptopals.com/sets/1/challenges/3

# You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.

import binascii

def decodeMe(s):
    decodedStr = binascii.unhexlify(s)
    
    # trying XOR of decoded string with all 256 ASCII characters and saving in a generator class
    strings = (''.join(chr(num ^ key) for num in decodedStr) for key in range(256))
    
    # do find the line with ETAOIN SHRDLU (max occuring english characters)
    return max(strings, key=lambda s: sum((26-i) * s.count(c) for i, c in enumerate('etaoinshrdlu')))

encodedStr = input("Plese enter the hex encoded string: ")
print(decodeMe(encodedStr))
