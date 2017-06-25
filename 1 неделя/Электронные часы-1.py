n = int(input())
minutes = (n % 60)
hours = (n // 60)
print(str(hours % 24), str(minutes))
