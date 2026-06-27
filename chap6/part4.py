# Định nghĩa một hàm con
def printerfunction(word1, word2):
    print("We got parameters", word1, "and", word2)

# Đây là hàm chính
def main():
    string_1 = "Blues record"
    string_2 = "Artichoke"

    # Gọi hàm con
    printerfunction(string_1, string_2)

# Đoạn mã này cho trình thông dịch biết
# tên của hàm chính khởi động chương trình

if __name__ == "__main__":
    main()