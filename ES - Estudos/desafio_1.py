print("Quantos passos você vai dar?")

quantidade_passos = int(input())

for i in range(quantidade_passos):
    print(f"voce deu {i} passos.")
    if quantidade_passos == 0:
        print("Nenhum passo dado na floresta.")
