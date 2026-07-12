"""
9 Thuộc tính riêng tư (Private attributes) – Phần 2

Ở phần trước, chúng ta đã biết rằng private attribute giúp bảo vệ dữ liệu khỏi việc bị thay đổi trực tiếp từ bên ngoài class. 
Tuy nhiên, điều này cũng tạo ra một vấn đề mới: vì thuộc tính đã được bảo vệ nên chúng ta không thể gán giá trị trực tiếp cho nó như trước.

May mắn là đây không phải là vấn đề lớn, vì các method bên trong class vẫn có thể truy cập và thay đổi private attribute một cách bình thường.
"""

"""
Nội dung chính của phần này
Private attribute vẫn có thể được thay đổi bên trong class thông qua các method.
Đây là cách an toàn để kiểm soát việc thay đổi dữ liệu.

Trong Python, private không hoàn toàn tuyệt đối vì có thể truy cập bằng cú pháp: object._ClassName__attribute
Cách truy cập này chỉ nên dùng trong những trường hợp đặc biệt và không được khuyến khích trong lập trình thông thường.
"""

# class Score:
#     __points = 0

#     def getpoints(self):
#         return self.__points

#     def addpoints(self, value=1):
#         self.__points += value


# Blue = Score()
# Blue.addpoints(3)
# print(Blue.getpoints())


class BankAccount:
    __balance = 0

    def deposit(self, money):
        self.__balance += money

    def show_balance(self):
        print(self.__balance)

acc = BankAccount()
acc.deposit(500)
acc.show_balance()

# acc._BankAccount__balance = 100000
# acc.show_balance() /100000