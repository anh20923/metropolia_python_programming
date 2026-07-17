"""
| Phương thức    | Chức năng                                | Ghi chú                                   |
| -------------- | ---------------------------------------- | ----------------------------------------- |
| `append(X)`    | Thêm `X` vào cuối list                   | Phổ biến nhất                             |
| `insert(I, X)` | Chèn `X` vào vị trí `I`                  | Các phần tử phía sau sẽ dịch sang phải    |
| `remove(X)`    | Xóa phần tử đầu tiên có giá trị `X`      | Phải biết giá trị                         |
| `pop(I)`       | Xóa phần tử ở vị trí `I`                 | Trả về phần tử vừa xóa                    |
| `index(X)`     | Trả về vị trí xuất hiện đầu tiên của `X` | Báo `ValueError` nếu không tìm thấy       |
| `count(X)`     | Đếm số lần `X` xuất hiện                 | Không báo lỗi nếu không có                |
| `sort()`       | Sắp xếp list theo thứ tự tăng dần        | Chuỗi được sắp theo bảng mã ASCII/Unicode |
| `reverse()`    | Đảo ngược thứ tự các phần tử             | Phần tử đầu thành cuối, cuối thành đầu    |

!!!
Lưu ý: sort() và reverse() thay đổi trực tiếp list gốc, chúng không tạo ra một list mới.
"""

# -*- coding: cp1252 -*-

# List như một biến

# Tạo mylist (chú ý xuống dòng khi khai báo)
mylist = ["Apples", "Milk",
          "Beer", "Squigg"]

print(mylist)

# Thêm một phần tử
mylist.append("Pineapple")
print(mylist)

# Xóa phần tử ở vị trí số 1
mylist.pop(1)

# In các phần tử còn lại
for i in mylist:
    print(i)


