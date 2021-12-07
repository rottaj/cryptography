hex_string = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

x = bin(int(hex_string, 16))[2:] # remove trailing c0
x2 = bin(int(hex_string2, 16))[2:]
trailing = len(x) if len(x) > len(x2) else len(x2)
x = x.zfill(trailing)
x2 = x2.zfill(trailing)
print(x, x2, "\n", len(x), len(x2))
c = "".join([str(int(i1) ^ int(i2)) for i1, i2 in zip(x, x2)])
print(hex(int(c, 2))[2:])

