def aes_in_ecb(c, k):
  print(c, k)

if __name__ == "__main__":

  k = "YELLOW SUBMARINE"
  with open("../datfile/aes_data.dat") as f:
    data = f.readlines()
    aes_in_ecb(data, k)
