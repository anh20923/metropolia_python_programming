"""
6 Phương thức của class (Class methods)

Class là một công cụ rất hữu ích, nhưng nếu không có method (phương thức) thì khả năng sử dụng của nó sẽ bị hạn chế. Khi kết hợp class với method, 
chúng ta mới bắt đầu tiếp cận đúng khái niệm của lập trình hướng đối tượng (Object-Oriented Programming - OOP), 
vì lúc này class không chỉ lưu dữ liệu mà còn có thể tự xử lý dữ liệu của chính nó.

Việc định nghĩa một method cũng không khó. Nếu attribute là biến thuộc về class thì method có thể được xem là hàm thuộc về class. 
Thực tế, method được tạo gần giống như một hàm thông thường (function), chỉ có một điểm khác biệt là tham số đầu tiên luôn là self, 
đây là tham số mà Python yêu cầu khi định nghĩa method.

Cần lưu ý rằng self không phải là từ khóa (keyword) của Python, mà chỉ là một quy ước đặt tên. Về mặt kỹ thuật, 
tham số đầu tiên này có thể có bất kỳ tên nào. Tuy nhiên, tài liệu chính thức của Python và hầu hết lập trình viên đều sử dụng tên self, 
vì vậy chúng ta cũng nên sử dụng tên này.

Ngoài điểm khác biệt đó, method được tạo giống hệt như một hàm bình thường, chỉ khác là nó được viết bên trong class.
"""

class Customer:
    name = "John Johnsson"
    total = 1000
    paymenttype = "Masterexpress"
    number = "1234-5678-9012345"

    def printout(self):
        print("Name:", self.name)
        print("Total:", self.total)
        print("Payment type:", self.paymenttype)
        print("Card/Bill number:", self.number)