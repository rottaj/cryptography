#v = "10101"
#z = "010111111111111100000
v = "01101101" # Key
z = "10110100" # p

trailing = len(z) if len(z) > len(v) else len(v)
v = v.zfill(trailing)
z = z.zfill(trailing)

print(trailing)
print(v, "\n", z, len(v), len(z))
# Encrypt
xor = "".join([str(int(x1) ^ int(x2)) for x1, x2 in zip(list(v),list(z))])
print("XOR'd", xor)
# Decrypt
p = "".join([str(int(x1) ^ int(x2)) for x1,x2 in zip(v, xor)])
print("\n\n", "Decrypted Phrase: ", p, "\n", "Phrase: ", z)

