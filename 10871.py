n, x = map(int, input().split())
var = input().split()
ans = []
for i in range(n):
    if int(var[i]) < x:
        ans.append(var[i])
print(" ".join(ans))








