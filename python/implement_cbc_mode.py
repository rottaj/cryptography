from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
BLOCK_SIZE = 16

def get_block(n, data): # get current block
  l = data[n:n+BLOCK_SIZE]
  return bytes(l.encode("utf8"))

def pad(blockList): # make sure block_size is currect
  if len(blockList) == BLOCK_SIZE:
    return b''.join(blockList)
  else:
    if (BLOCK_SIZE - len(blockList)) % 4 == 0:
      blockList.append(b"\04")
    elif (BLOCK_SIZE - len(blockList)) % 2 == 0:
      blockList.append(b"\02")
    elif (BLOCK_SIZE - len(blockList)) % 1 == 0:
      blockList.append(b"\01")
    return pad(blockList)


def encrypt_ecb(block, key):
  cipher = AES.new(key, AES.MODE_ECB)
  cipherText = cipher.encrypt(block)
  return cipherText


def decrypt_ecb(cipherText, key):
  cipher = AES.new(key, AES.MODE_ECB)
  plainText = cipher.decrypt(cipherText)
  return plainText



def implement_ecb(data, key): ## Each block is encrypted w/ same key.
  cipherText = []
  for i in range(0, len(data), BLOCK_SIZE): # step every 16 bytes
    x = get_block(i, data)
    x = pad([bytes(i.encode("utf8")) for i in x.decode()])
    c = encrypt_ecb(x, key)
    cipherText.append(c)
  return b''.join(cipherText)

def xor(block, iv):
  print("TESTING", int(block, 2) ^ int(iv, 2))

def implement_cbc(data, key, iv): ## ECB but xored agains previous block
  cipherText = []
  for i in range(0, len(data), BLOCK_SIZE): # step every 16 bytes
    if i ==0: # initialize vector
      x = get_block(i, data)
      x = pad([bytes(i.encode("utf8")) for i in x.decode()])
      print(x)
      t = [(int(x1, 10) ^ int(x2, 10)) for x1, x2 in zip(x, iv)]
      print(t)

    else:
      x = get_block(i, data)
      x = pad([bytes(i.encode("utf8")) for i in x.decode()])
      print(x)
      c = encrypt_ecb(x, key)
      print(c)

      



if __name__ == "__main__":
  key = b"YELLOW SUBMARINE"
  data = []
  with open("../datfile/10_special.dat") as f:
    data = ''.join([d[:len(d)-1] for d in f.readlines()])
  ct = implement_ecb(data, key)
  pt = decrypt_ecb(ct, key)
  print("\n\nCipher Text after Encrypted: ", ct, "\n")
  print("Plain Text after Decrypted: ", pt, "\n\n\n")
  
  print("\n\n===========================================================\n\n")
  iv = b'\x00\x00\x00 &c' #initialization vector
  implement_cbc(data, key, iv)


'''   
if __name__ == "__main__":


  key = b"YELLOW SUBMARINE"
  data = []
  with open("../datfile/10.dat") as f:
    data = f.readlines()
    data = ''.join([d[:len(d)-1] for d in data])
  # Iterate through blocks
  #currentKey = ecb(data[0]) #initialization vector
  for i in range(0, len(data)):
    x = get_block(i, data)
    if len(x) != BLOCK_SIZE:
      x = pad([bytes(b.encode("utf8")) for b in str(x)[2:]])
      break

    currentKey = ecb(x, key) 
    print(currentKey)
'''
