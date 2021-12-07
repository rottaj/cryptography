hex_string = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

x = bin(int(hex_string, 16))[2:]
x2 = bin(int(hex_string, 16))[2:]
print(x, x2, "\n", len(x), len(x2))

fill_zeros = len(x) if len(x) > len(x2) else len(x2)
x = x.zfill(fill_zeros)
x2 = x2.zfill(fill_zeros)

new = [int(bit1) ^ int(bit2) for bit1, bit2 in zip(list(x), list(x2))]
print("\n", new)
res = "".join([str(i) for i in new])
print("\n\n", res)

