# Đây là mã ở MAIN LEVEL
print("Main level code!")

def subfunction():
    # Đây là mã trong SUBFUNCTION
    print("Subfunction code!")

def main():
    # Đây là mã trong MAIN FUNCTION
    print("Main function code!")

# Cấu trúc này cho Python biết
# đâu là hàm bắt đầu chương trình

if __name__ == "__main__":
    subfunction()
    main()