hex_string = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

a_string = bytes.fromhex(hex_string)
a_stringTwo = bytes.fromhex(hex_string2)
val_new = int.from_bytes(a_string, "big")
val_new2 = int.from_bytes(a_stringTwo, "big")
print(len(list(str(val_new))), len(list(hex_string2)))
print(list(str(val_new)), "\n\n", list(hex_string2))
print(int(val_new) ^ int(val_new2))
