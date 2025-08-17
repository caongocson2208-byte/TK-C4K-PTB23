# for i in range(5):
#     print("Sơn abc")

# a = int(input("Nhập vào số a: "))
# b = int(input("Nhập vào số b: "))
# sum = 0
# if a % 2 == 1:
#     a += 1  
# for i in range(a, b, 2):
#     sum += i
# print(f"Tổng các số chẵn từ {a} đến {b} là: {sum}")

# a = int(input("Nhập vào số a: "))
# for i in range(1, 11):
#     print(f'{a} x {i} = {a * i}')

from math import sqrt

num = int(input("Nhập vào số num: "))

if num < 2:
    print(f"{num} không phải là số nguyên tố")
else:
    is_prime = True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            print(f"{num} không phải là số nguyên tố")
            is_prime = False
            break
    if is_prime == True:
        print(f"{num} là số nguyên tố")
