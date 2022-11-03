t = int(input())
for _ in range(t):
    ox = input()
    point, count = 0, 1
    for i in ox:
        if i == "O":
            point += count
            count += 1
        else:
            count = 1    
    print(point)
