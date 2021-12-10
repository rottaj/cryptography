
def repeating_xor(p, k): # C = E(P, K)
  counter = 0
  xored = []
  for i in p:
    if counter == len(k):
      xored.append(hex(i ^ k[counter-1])[2:])
      counter=0
    else:
      xored.append(hex(i ^ k[counter])[2:])
    counter+=1
  return "".join(xored)

if __name__ == "__main__":
  p = (b"Burning 'em, if you ain't quick and nimble\n"
        b"I go crazy when I hear a cymbal")
  k = b"ICE"

  
  print(p)
  cipherText = repeating_xor(p, k)
  print("\n\n", cipherText, "\n\n")
  plainText = repeating_xor(bytes(cipherText, "utf-8"), k)
  print("\n\n", str(plainText), "\n\n")

  




