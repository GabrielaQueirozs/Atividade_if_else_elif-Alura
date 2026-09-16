atividadeA = int(input("Digite o total de dias da atividade A:"))
atividadeB =int(input("Digite o total de dias da atividade B:"))
atividadeC = int(input("Digite o total de dias da atividade C:"))

if(atividadeA >=0 and atividadeB >=0 and atividadeC >=0):
    tempo_total = atividadeA+atividadeB+atividadeC
    print(f"O tempo total é de {tempo_total} dias")
else:
    print("erro: os dias não podem ser negativos")