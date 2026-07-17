"""
| Cú pháp               | Ý nghĩa                                |
| --------------------- | -------------------------------------- |
| `"A" in mylist`       | Kiểm tra `"A"` có trong list không     |
| `for item in mylist:` | Duyệt trực tiếp từng phần tử của list  |
| `range(len(mylist))`  | Duyệt theo **chỉ số (index)** của list |
| `append()`            | Thêm phần tử vào cuối list             |
| `len(mylist)`         | Đếm số phần tử trong list              |

"""
#1. Kiểm tra phần tử có trong list bằng in
basket = ["Apples", "Orange", "Kiwifruit", "Banana"]

print("Cauliflower" in basket)
print("Apples" in basket)
########################################################################

#2. Duyệt list bằng for
mylist = [1, 2, 3, 4]

for i in mylist:
    print(i)
########################################################################


#3. Tạo list mới từ list cũ
mylist = [1, 2, 3, 4]
newlist = []

for i in mylist:
    newlist.append(i + 10)

print(newlist)
########################################################################


#4. Duyệt list theo chỉ số (index)
mylist = [1, 2, 3, 4]
for i in range(len(mylist)):
    print(i, mylist[i])
########################################################################



#5. So sánh hai cách dùng for
##Cách 1 (khuyên dùng khi không cần index)
mylist = ["Apple", "Banana", "Orange"]
for fruit in mylist:
    print(fruit)


##Cách 2 (khi cần index)
mylist = ["Apple", "Banana", "Orange"]
for i in range(len(mylist)):
    print(i, mylist[i])
########################################################################


#6. in kết hợp với if
basket = ["Apple", "Banana", "Orange"]
if "Banana" in basket:
    print("Có chuối")
if "Kiwi" not in basket:
    print("Không có kiwi")