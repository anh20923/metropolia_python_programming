"""
| Cú pháp                  | Ý nghĩa                            |
| ------------------------ | ---------------------------------- |
| `import pickle`          | Nạp module pickle                  |
| `open("file.dat","wb")`  | Mở file để ghi dữ liệu nhị phân    |
| `pickle.dump(obj, file)` | Lưu đối tượng vào file             |
| `"wb"`                   | Write Binary (ghi file nhị phân)   |
| `"w"`                    | Write Text (không dùng với pickle) |
!!!!
Ghi nhớ
pickle dùng để lưu toàn bộ đối tượng Python (list, dictionary, tuple, set, object...) xuống file.
File phải mở ở chế độ "wb".
File .dat tạo ra là file nhị phân, không đọc hay chỉnh sửa bằng trình soạn thảo văn bản.
Sau này, để đọc lại dữ liệu đã lưu, bạn sẽ dùng hàm pickle.load() (được giới thiệu ở phần tiếp theo).
"""

import pickle

listexample = [
    "Pineapple",
    "Atlas",
    ("Shaft", "Blade"),
    1150
]

filename = open("saveme.dat", "wb")

print(listexample)

pickle.dump(listexample, filename)

filename.close()