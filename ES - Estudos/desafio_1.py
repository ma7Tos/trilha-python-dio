quantidade_passos = int(input())

if quantidade_passos <= 0:
        print("Nenhum passo dado na floresta.")
else:
    for i in range(quantidade_passos):
        if(i == 0):
            print("Explorador:",i+1, "passo")
        else:
            print("Explorador:",i+1, "passos")