p = (b"Burning 'em, if you ain't quick and nimble\n"
      b"I go crazy when I hear a cymbal")
k = b"ICE"

counter = 0
xored = []
for i in p:
  if counter == len(k):
    xored.append(hex(i ^ k[counter-1])[2:])
    counter=0
  else:
    xored.append(hex(i ^ k[counter])[2:])
  counter+=1
print("\n\n\nxored: ", "".join(xored))
