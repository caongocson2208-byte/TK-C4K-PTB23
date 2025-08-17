# num = int(input("Nhập vào một số nguyên: "))

# if num % 2 == 0:
#     print(f"{num} là số chẵn.")
# elif num % 2 == 1:
#     print(f"{num} là số lẻ.")
# else:
#     print("Đầu vào không phải là một số nguyên hợp lệ.")


avg = float(input("Nhập vào điểm trung bình: "))

if avg >= 8 and avg <= 10: 
    print("- Học sinh giỏi")
elif avg >= 6 and avg < 8:
    print("- Học sinh khá")
elif avg >= 5 and avg < 6:
    print("- Học sinh trung bình")
elif avg >= 0 and avg < 5:
    print("- Học sinh yếu")
else:
    print("- Điểm trung bình không hợp lệ")


name = input("Nhập vào tên của bạn: ")
age = int(input("Nhập vào tuổi của bạn: "))

if age >= 18:
    print(f"Chào mừng {name} đến với trang web")
else:
    print(f"Xin lỗi {name}, bạn chưa đủ tuổi để truy cập trang web")