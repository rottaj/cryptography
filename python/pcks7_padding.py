
def pkcs_padding(plainText):
  textArr = list(plainText)
  if len(textArr) % 4 == 0:
    i = 0
    while i <= len(textArr) / 4:
      textArr.append("\x04")
      i +=1
  elif len(textArr) % 2 == 0:
    i = 0
    while i <= len(textArr) / 2:
      textArr.append("\x02")
      i +=1
  elif len(textArr) % 3 == 0:
    i = 0
    while i <= len(textArr) / 3:
      textArr.append("\x03")
      i +=1

  return ''.join(textArr)

if __name__ == "__main__":
  plainText = "YELLOW SUBMARINE"
  cipherText = pkcs_padding(plainText)
  print(cipherText, len(cipherText))
