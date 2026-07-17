"""
| Phương thức | Chức năng                                      |
| ----------- | ---------------------------------------------- |
| `[]`        | Tạo list rỗng                                  |
| `append(x)` | Thêm phần tử `x` vào cuối list                 |
| `remove(x)` | Xóa phần tử có giá trị `x` (phải biết giá trị) |
| `pop(i)`    | Xóa phần tử ở vị trí `i` và trả về phần tử đó  |
| `pop()`     | Xóa phần tử cuối cùng và trả về phần tử đó     |
| `list[i]`   | Truy cập phần tử ở vị trí `i` (bắt đầu từ 0)   |

"""


mylist = []
mylist.append("oneitem")
mylist.append(123131)

mylist.remove("oneitem")

print(mylist)