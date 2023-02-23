n = 3
c = '*'

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print(c * (2 * i - 1))
