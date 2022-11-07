fix, var, price = map(int, input().split())
total_cost = fix + var
income = 0
count = 0
cnt = 0
while income > total_cost:
    income += price * count
    cnt += 1

print(cnt)












