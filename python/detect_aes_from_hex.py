from Crypto.Cipher import AES

def detect_aes_from_hex(data):
  for i in range(len(data)):
    byteString = bytes.fromhex(data[i]) 
    l = [byteString[b:b+16] for b in range(0, len(byteString), 16)]
    list_set = set(l)
    repeated = len(l) - len(list_set) # get total blocks subtracted by repeated blocks
    if repeated > 0:
      print("FOUND", i)
      print("LIST SET", str(list_set))
      break


if __name__ == "__main__":
  data = []
  with open("./detect_aes_from_hex.dat") as f:
    data = f.readlines()
  for i in range(len(data)):
    data[i] = data[i][:len(data[i])-1]
  detect_aes_from_hex(data)

