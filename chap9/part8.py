"""
Một private attribute được khai báo giống như thuộc tính thông thường, nhưng tên của nó phải bắt đầu bằng ít nhất hai dấu gạch dưới (__):

__attribute_name

Ví dụ:

__points
__score
__getsome

đều là các tên hợp lệ.
"""


class Score:
    __points = 0 #private attribute

    def getpoints(self):
        return self.__points
    


    
class Student:
    __score = 0

    def add_score(self):
        self.__score += 10

    def show_score(self):
        print(self.__score)

s = Student()
s.add_score()
s.show_score()