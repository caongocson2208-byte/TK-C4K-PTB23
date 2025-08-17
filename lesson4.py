# a = float(input("Nhập vào số a: "))
# b = float(input("Nhập vào số b: "))

# if a == 0:
#     if b == 0:
#         print("Vô số nghiệm")
#     else:
#         print("Vô nghiệm")
# else:
#     x = -b / a
#     print(x)

from math import sqrt
a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
else:
    dt = b*b - 4*a*c
    if dt < 0:
        print("Phương trình vô nghiệm")
    elif dt == 0:
        x = -b / (2 * a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        x1 = (-b + sqrt(dt)) / (2 * a)
        x2 = (-b -sqrt(dt)) / (2 * a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")


