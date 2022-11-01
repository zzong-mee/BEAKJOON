n = int(input())

for i in range(10):
    if i == 0:
        continue
    
    num = n * i
    print(f"{n} * {i} = {num}")