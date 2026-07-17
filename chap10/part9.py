"""
| Cú pháp                 | Ý nghĩa                         |
| ----------------------- | ------------------------------- |
| `import pickle`         | Nạp module pickle               |
| `open("file.dat","wb")` | Mở file để ghi dữ liệu nhị phân |
| `pickle.dump(obj,file)` | Lưu đối tượng vào file          |
| `open("file.dat","rb")` | Mở file để đọc dữ liệu nhị phân |
| `pickle.load(file)`     | Đọc đối tượng từ file           |

"""

import pickle

file = open("saveme.dat","rb")

numbers = pickle.load(file)

print(numbers)

file.close()