n = int(input())

number = 1
sum_squares = 0

while number <= n:
    sum_squares += number ** 2
    number += 1

print(sum_squares)
