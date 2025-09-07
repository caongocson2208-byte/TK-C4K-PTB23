# import math

# a = int(input("Nhập số nguyên dương a: "))
# b = int(input("Nhập số nguyên dương b: "))

# gcd = math.gcd(a, b)
# lcm = a * b / gcd
# print("Bội chung nhỏ nhất của", a, "và", b, "là:", lcm)

# x = a / gcd
# y = b / gcd
# print("Phân số tối giản", x, y)

animals = ["cat", "dog", "elephant", "tiger", "lion", "monkey"]
# Độ dài danh sách
print(len(animals)) # Bắt đầu từ 1
# In toàn bộ danh sách
print(animals)
# In vị trí bất kỳ trong danh sách
print(animals[2]) # elephant
# In đầu danh sách 
print(animals[0]) # cat
# In cuối danh sách
print(animals[-1]) # monkey
# In từng phần tử trong danh sách
for i in range(len(animals)):
   print(animals[i])



