import binascii
import base64

str = input("Enter your hex: ")

print("\nconvering to raw bytes...")
bin = binascii.unhexlify(str);
print("Raw data- ",bin.decode("utf-8"))

print()

print("\nencoding in base64...")
b64 = base64.b64encode(bin)
print("Base64 encoded - ",b64.decode("utf-8"))

