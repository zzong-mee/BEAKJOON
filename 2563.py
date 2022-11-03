n = int(input())
paper = [[0 for col in range(101)] for row in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[a+i][b+j] = 1

area = 0
for i in paper:
    area += sum(i)
print(area)

