"""
Python tự động tạo nhiều thuộc tính và phương thức đặc biệt có dạng __ten__.
__init__() là constructor, tự động chạy khi object được tạo.
__doc__ lưu docstring của class.
__class__ cho biết object được tạo từ class nào.
Những thuộc tính đặc biệt này giúp Python quản lý object và hỗ trợ nhiều cơ chế hoạt động của ngôn ngữ.
"""

# #1 __init__
# class Student:
#     def __init__(self):
#         print("A new student was created!")

# s = Student()


# #2 __doc__
# class Empty:
#     """This class is empty"""
#     pass

# keg =Empty()
# print(keg.__doc__)


# #3 __class__
# class Customer:
#     pass

# c = Customer()
# print(c.__class__)


#VD tong hop
class Student:
    """Student class"""

    def __init__(self):
        print("Student created")

s = Student()
print(s.__doc__)
print(s.__class__)