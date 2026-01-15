z = int(input())
b = int(input())
total3 = 0
total2 = 0
for i in range(z, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        total3 = total3 + 1
print(total3)






