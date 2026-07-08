class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
    



"""
Ví dụ kết hợp với try-except
Lỗi tự tạo cũng có thể được bắt:

class AgeError(Exception):
    pass


age = -5

try:
    if age < 0:
        raise AgeError("Age cannot be negative")

except AgeError as e:
    print(e)
"""