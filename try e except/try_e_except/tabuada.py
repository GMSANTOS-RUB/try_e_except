try:
    numero = int(input("Digite um número inteiro: "))
except:
    print("Erro: você deve digitar um número inteiro válido.")
print(f"tabuada do numero {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")