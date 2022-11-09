n = int(input())

def hanoi(x, y, z, cnt):
    if cnt == 0:
        return

    hanoi(x, z, y, cnt - 1)
    print(x,z)
    hanoi(y, x, z, cnt - 1)

print((2**n) - 1)

if n <= 20:
    hanoi(1, 2, 3, n)