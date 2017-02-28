# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.


# replace string with the input hex string
STRING="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# coverting hex to binary and then to base64
echo $STRING | xxd -r -p | base64
