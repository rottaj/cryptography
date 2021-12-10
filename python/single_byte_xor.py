import sys

def find_byte_xor(key):
  hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
  split = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
  print(split)
  print(int(split[0], 16) ^ int(key, 36))
  testing = "".join([bin(int(i, 16) ^ int(key, 36)) for i in split])
  print(hex(int(testing, 2)[2:]))
  '''
  decimals = "".join([bin(int(i, 16) ^ int(key, 16))[2:] for i in hex_string])
  ret = hex(int(decimals, 2))[2:]
  return ret
  '''
if __name__ == "__main__":
  key = sys.argv[1]
  find_byte_xor(key)
  #sys.stdout.write(ret)


