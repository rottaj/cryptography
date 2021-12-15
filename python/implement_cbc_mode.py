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
    print(len(blockList), blockList, BLOCK_SIZE - len(blockList))
    if BLOCK_SIZE - len(blockList) % 4 == 0:
      blockList.append(b"\04")
    elif BLOCK_SIZE - len(blockList) % 2 == 0:
      blockList.append(b"\02")
    elif BLOCK_SIZE - len(blockList) % 1 == 0:
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
    if len(x) != BLOCK_SIZE:
      x = pad([bytes(b.encode("utf8")) for b in str(x)])
      c = encrypt_ecb(x, key)
      cipherText.append(c)
      break
    else:
      c = encrypt_ecb(x, key)
      cipherText.append(c)
      
  return b''.join(cipherText)

 

def implement_cbc(data, key): ## ECB but xored agains previous block
  print(data)
  cipherText = []
  for i in range(0, len(data), BLOCK_SIZE): # step every 16 bytes
    x = get_block(i, data)
    test = [bytes(b.encode("utf8")) for b in str(x)]
    print(test, len(test))

      



if __name__ == "__main__":
  key = b"YELLOW SUBMARINE"
  data = []
  with open("../datfile/10_special.dat") as f:
    data = ''.join([d[:len(d)-1] for d in f.readlines()])
  ct = implement_ecb(data, key)
  pt = decrypt_ecb(ct, key)
  print("\n\nCipher Text after Encrypted: ", ct, "\n")
  print("Plain Text after Decrypted: ", pt, "\n\n\n")

  implement_cbc(data, key)


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
