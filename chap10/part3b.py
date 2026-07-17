
# 1. Tạo Dictionary
print("===== Ví dụ 1: Tạo Dictionary =====")
fruits = {
    "A": "Apples",
    "O": "Oranges"
}
print(fruits)



# 2. Truy cập giá trị bằng key
print("\n===== Ví dụ 2: Truy cập bằng key =====")
fruits = {
    "A": "Apples",
    "O": "Oranges"
}
print(fruits["A"])



# 3. Dictionary có nhiều cặp key-value
print("\n===== Ví dụ 3: Dictionary nhiều phần tử =====")
country = {
    "FI": "Finland",
    "VN": "Vietnam",
    "JP": "Japan"
}
print(country["VN"])
print(country["JP"])



# 4. Chuyển chữ sang mã Morse
print("\n===== Ví dụ 4: Chuyển sang mã Morse =====")
alphabet = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..'
}

word = "bach"
result = ""
for i in range(len(word)):
    result += alphabet[word[i]] + "/"
print(result)



# 5. Hàm chuyển đổi sang Morse
print("\n===== Ví dụ 5: Hàm chuyển sang mã Morse =====")
def morsecoder(word):

    alphabet = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..'
    }

    result = ""

    for i in range(len(word)):
        result += alphabet[word[i]] + "/"
    print("Word", word, "in Morse code is")
    print(result)

morsecoder("cliff")
morsecoder("bach")



# 6. Duyệt Dictionary bằng key
print("\n===== Ví dụ 6: Duyệt key =====")
country = {
    "FI": "Finland",
    "VN": "Vietnam",
    "JP": "Japan"
}
for key in country:
    print(key)



# 7. Duyệt Dictionary lấy cả key và value
print("\n===== Ví dụ 7: Duyệt key và value =====")
country = {
    "FI": "Finland",
    "VN": "Vietnam",
    "JP": "Japan"
}

for key in country:
    print(key, "->", country[key])



# 8. Thêm phần tử mới
print("\n===== Ví dụ 8: Thêm phần tử =====")
country = {
    "FI": "Finland"
}
country["VN"] = "Vietnam"
print(country)



# 9. Sửa giá trị
print("\n===== Ví dụ 9: Sửa giá trị =====")
country = {
    "FI": "Finland"
}
country["FI"] = "Suomi"
print(country)



# 10. Xóa phần tử
print("\n===== Ví dụ 10: Xóa phần tử =====")
country = {
    "FI": "Finland",
    "VN": "Vietnam"
}
del country["VN"]
print(country)