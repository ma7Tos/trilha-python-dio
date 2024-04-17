capacidade_atual, aumento_percentual = map(int, input().split())

capacidade_total = capacidade_atual + (capacidade_atual * aumento_percentual) / 100
print(int(capacidade_total))