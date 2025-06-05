try:
    peso = float(input("\nDigite seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))
except ValueError:
    print("Erro: você deve digitar números válidos para peso e altura.")
else:
    imc = peso/(altura ** 2)
    print(f"seu IMC é:) {imc:.2f}")

    # Interpretar o resultado do IMC
    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif 18.5 <= imc < 25:
        print("Peso normal.")
    elif 25 <= imc < 30:
        print("Sobrepeso.")
    else:
        print("Obesidade.")
