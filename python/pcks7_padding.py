
def pad(byteList, padding, b):
  if len(byteList) == padding:
    return byteList
  else:
    byteList.append(b)
    return pad(byteList, padding, b)


def pkcs_padding(plainText, padding):
  l = [bytes(i.encode("utf8")) for i in list(plainText)]
  if (padding - len(l)) % 4 == 0:
    byteList = pad(l, padding, b"\04")
  elif (padding - len(l)) % 2 == 0:
    byteList = pad(l, padding, b"\02")

  return b''.join(byteList)

if __name__ == "__main__":
  plainText = "YELLOW SUBMARINE"
  cipherText = pkcs_padding(plainText, 22)
  print(cipherText)
