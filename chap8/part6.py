"""
Khác nhau giữa try-except và try-finally
|                      | try-except                        | try-finally                                         |
| -------------------- | --------------------------------- | --------------------------------------------------- |
| Mục đích             | Bắt và xử lý lỗi                  | Thực hiện hành động trước khi chương trình kết thúc |
| Ngăn crash?          | Có                                | Không                                               |
| Có xử lý lỗi cụ thể? | Có (`ValueError`, `TypeError`...) | Không                                               |
| Luôn chạy?           | Không                             | Có                                                  |

"""