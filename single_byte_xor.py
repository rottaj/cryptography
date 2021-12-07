hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

hex_vals = [int(i, 16) for i in hex_string]
print(hex_vals, "\n")
xor_vals = [i ^ 3 for i in hex_vals]
print(xor_vals)
ret = ''.join([hex(i) for i in hex_vals])
print("\n", ret)
