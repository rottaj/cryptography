hex_string = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

a_string = bytes.fromhex(hex_string)
a_string2 = bytes.fromhex(hex_string2)
print(a_string, '\n', a_string2)
val_new = int.from_bytes(a_string, "big")
val_new2 = int.from_bytes(a_string2, "big")
print("\n\n", val_new, "\n", val_new2)

print(len(list(str(val_new))), len(list(str(val_new2))))

list_nums = list(str(val_new))
list_nums2 = list(str(val_new2))
xored = ''.join([str(int(list_nums[i]) ^ int(list_nums2[i])) for i in range(0, len(list_nums))])
print(xored)
