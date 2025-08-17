# i = 3
# while (i < 5):
#     print("Sơn abc")
#     i += 1

# n = int(input("Nhập vào số n: "))
# while n < 0 or n > 100: 
#     n = int(input("Vui lòng nhập n từ 0 - 100: "))
# for i in range(n, 101):
#     print(i)

n = int(input("Nhập vào số n: "))
i = 1
sum = 0 
while sum <= n: 
    sum += i
    i += 1
print(f"Tổng các số từ 1 đến {i-1} là: {sum}")    
