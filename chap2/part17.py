bigstring = "Damn the torpedoes, full speed ahead!"
length = len(bigstring)

print("The length of the string is", length, "characters.")

slice_1 = bigstring[:15]
slice_2 = bigstring[15:]
slice_3 = bigstring[::2]

slice_4 = bigstring[1]
slice_5 = bigstring[5:26]
slice_6 = bigstring[::-1]

slice_7 = bigstring[-10:]
slice_8 = bigstring[:-10]
slice_9 = bigstring[4:30:2]

# print("slice_1:", slice_1)
# print("slice_2:", slice_2)
# print("slice_3:", slice_3)
# print("slice_4:", slice_4)
# print("slice_5:", slice_5)
# print("slice_6:", slice_6)
# print("slice_7:", slice_7)
# print("slice_8:", slice_8)
# print("slice_9:", slice_9)
print(bigstring[-3:])

"""
✅ [:n] = lấy n ký tự đầu

✅ [n:] = lấy từ vị trí n đến hết

✅ [-n:] = lấy n ký tự cuối
"""