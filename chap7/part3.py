"""
| Tên          | Chức năng                                                                 |
| ------------ | ------------------------------------------------------------------------- |
| **random**   | Sinh số ngẫu nhiên, chọn ngẫu nhiên.                                      |
| **math**     | Các hàm toán học, ma trận.                                                |
| **pickle**   | Đọc và ghi các cấu trúc dữ liệu động như **list** hoặc **class** vào tệp. |
| **sys**      | Các hàm liên quan đến dịch vụ của hệ điều hành.                           |
| **zipfile**  | Tạo và thao tác với các tệp nén ZIP.                                      |
| **tkinter**  | Tạo giao diện đồ họa (xem Chương 11).                                     |
| **winsound** | Phát âm thanh (chỉ có trên Windows).                                      |
| **time**     | Các hàm về thời gian, lịch và tính toán thời gian.                        |
| **os**       | Cung cấp thêm các hàm làm việc với hệ điều hành.                          |

"""

import sys

startprice = int(input("Please input the price: "))

if startprice < 0:
    print("Please, no negative numbers.")
    sys.exit(0)
else:
    tax = int(input("Please insert the VAT % (0-100): "))

if tax < 0:
    print("VAT cannot be less than 0.")
    sys.exit(0)

print("Final price is", startprice * (tax / 100) + startprice)