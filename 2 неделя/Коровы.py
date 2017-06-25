n = int(input())
if n < 100:
    if 5 <= n <= 20 or (n % 10) >= 5 or (n % 10 == 0):
        print(n, 'korov')
    elif n % 10 == 1:
        print(n, 'korova')
    else:
        print(n, 'korovy')
