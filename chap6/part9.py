def square(width=float(5.0), height=float(8.0)):
    area = width * height
    return area

def main():
    # Vì bây giờ các tham số đã có giá trị mặc định,
    # nên chúng ta có thể bỏ qua một số tham số khi gọi hàm.

    area1 = square()
    area2 = square(4.0, 3.0)
    area3 = square(10.0)
    area4 = square(height=11.0)

    print("Four different ways of calling our function...")
    print("And they all work:")
    print(area1, area2, area3, area4)

if __name__ == "__main__":
    main()