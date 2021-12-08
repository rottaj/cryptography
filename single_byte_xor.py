import sys

def find_byte_xor(key):
  hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
  key_hash = str(key) * len(hex_string)
  print(len(hex_string), len(key_hash))
  x1 = bin(int(hex_string, 16))[2:] #hexidecimal (base 16) to binary
  x2 = bin(int(key_hash, 10))[2:] #decimal (base 10) to binary
  x2 = x2.zfill(len(x1))
  print(x1, "\n\n", x2, "\n")
  print(len(x1), len(x2))
  c = "".join([str(int(i1) ^ int(i2)) for i1, i2 in zip(x1, x2)])
  ret = str(hex(int(c, 2))[2:])
  return ret

if __name__ == "__main__":
  print("ENTER KEY: ")
  key = input()
  ret = find_byte_xor(key)
  sys.stdout.write(ret)


