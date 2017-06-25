A = int(input())
B = int(input())
N = int(input())
translPenCost = (N * A * 100) + (N * B)
costRub = translPenCost // 100
cosPen = translPenCost % 100
print(costRub, cosPen)
