text = "This text has a line change.\n"
print(text)


rawtext = repr(text)
print(rawtext)

""" 
print(text) = hiển thị nội dung cho người dùng đọc.
print(repr(text)) = hiển thị "bên trong" chuỗi thực sự chứa những ký tự gì, rất hữu ích khi debug chương trình.
"""