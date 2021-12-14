from Crypto.Cipher import AES

def aes_in_ecb(c, k):
  cipher = AES.new(k.encode("utf8"), AES.MODE_ECB)
  plainText = cipher.decrypt(c.encode("utf8"))
  print(str(plainText))
  print(plainText.decode("latin-1").encode("utf-8"))


if __name__ == "__main__":

  k = "YELLOW SUBMARINE"
  with open("../datfile/aes_base64.dat") as f:
    data = f.readlines()
    print(''.join(data)) 
    aes_in_ecb(''.join(data), k)
