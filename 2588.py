num1 = int(input())
num2 = list(map(int, input()))
num2.reverse()
for i in num2:
    print(i * num1)
num2 = str(num2[2]) + str(num2[1]) + str(num2[0])
num6 = num1 * int(num2)
print(num6)