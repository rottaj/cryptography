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

def decrypt_cbc(cipherText, key, iv):
  cipher = AES.new(key, AES.MODE_CBC)
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


def xor_and_return_cipher(pt, ct): # xors --> returns cipherText
  return ''.join([chr(int(bin(i1), 2) ^ int(bin(i2), 2)) for i1, i2 in zip(pt, ct)])


def implement_cbc(data, key, iv): ## ECB but xored agains previous block
  cipherText = []
  for i in range(0, len(data), BLOCK_SIZE): # step every 16 bytes
    if i ==0: # initialize vector
      x = get_block(i, data)
      x = pad([bytes(i.encode("utf8")) for i in x.decode()])
      z = xor_and_return_cipher(x, iv)
      z = pad([bytes(i.encode("utf8")) for i in x.decode()])
      c = encrypt_ecb(z, key)     
      cipherText.append(c)

    else:
      x = get_block(i, data)
      x = pad([bytes(i.encode("utf8")) for i in x.decode()])
      z = xor_and_return_cipher(x, cipherText[-1])
      z = pad([bytes(i.encode("utf8")) for i in x.decode()])
      c = encrypt_ecb(x, key)
      cipherText.append(c)
  
  return b''.join(cipherText)


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
  ctCbc = implement_cbc(data, key, iv)
  print("CBC CIPHERTEXT: ", ctCbc) 
  ptCbc = decrypt_cbc(ctCbc, key, iv)
  print("DECRYPTED: ", ptCbc)
