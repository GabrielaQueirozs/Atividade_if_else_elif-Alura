peso = float(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura:"))

## para ele entender como calcular o imc
imc = peso / (altura**2)
print(f"Seu imc é : {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc < 25:
    print("Peso dentro do padrão")
else:
    print("Você está acima do peso")
    


