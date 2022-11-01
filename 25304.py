x = int(input())
n = int(input())
obj = []
for i in range(n):
    obj.append(list(map(int, input().split())))
sum = 0
for i in range(n):
    sum += obj[i][0] * obj[i][1]
if x == sum:
    print("Yes")
else:
    print("No")