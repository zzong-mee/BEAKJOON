num = []
for i in range(9):
    row = list(map(int, input().split()))
    num.append(row)

max_value = max(map(max, num))
loc=[[i, j] for i in range(9) for j in range(9) if num[i][j] == max_value]

print(max(map(max, num)))
print(loc[0][0]+1, loc[0][1]+1)
