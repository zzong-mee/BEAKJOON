num = input("").split(" ")
num = list(map(int, num))

answer = [1, 1, 2, 2, 2, 8]

for i in range(6):
    if num[i] > answer[i]:
        dfrn = num[i] - answer[i]
        num[i] = -dfrn

    elif num[i] < answer[i]:
        dfrn = answer[i] - num[i]
        num[i] = dfrn

    elif num[i] == answer[i]:
        num[i] = 0

num = list(map(str, num))

print(f"{num[0]} {num[1]} {num[2]} {num[3]} {num[4]} {num[5]}")