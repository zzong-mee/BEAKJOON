t = int(input())

def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n-1)

for _ in range(t):
    k = int(input())
    n = int(input())

    print(int(factorial(k + n)/(factorial(k + 1)*factorial(n - 1))))







