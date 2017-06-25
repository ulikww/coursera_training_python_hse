n = int(input())
all_minutes = (n // 60)
hours = (n // 3600)
sec = (n % 60)
minutes = all_minutes % 60
print('{:d}:{:02d}:{:02d}'.format(hours % 60, minutes % 60, sec))
