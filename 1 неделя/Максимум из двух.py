a = int(input())
b = int(input())
c = a // b
f = 3 * c // (3 * c - 1)
print(a * f + b * (1 - f))
