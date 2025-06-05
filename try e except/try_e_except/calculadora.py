# 1.passo | mostrar o menu de opcões de aritmética(+, -, *, /)
# 2.passo | receber a pção escolhida oelo usuário
# 3.passo | receber os números a serem operados
# 4.passo | try e except para trocar erros

print("1 - soma")
print("2 - subtração")
print("3 - divisão")
print("4 - multiplicação")

codigo_calculadora = int(input("digite o codigo:"))

match codigo_calculadora:
    case 1:
        try:
            num1= int(input("Digite o primeiro numero a ser somado:"))
            num2= int(input("digite o segundo numero a ser somado:"))
            soma = num1+num2
            print(f"a soma do numero são {soma}")
        except:
           print("ocorreu um erro durante a operação< tente novamente!")

    case 2:
        try:
            num1= int(input("Digite o primeiro numero a ser subtraido:"))
            num2= int(input("digite o segundo numero a ser subtraido:"))
            subtração = num1+num2
            print(f"a subtração do numero sao {subtração}") 
        except:
           print("ocorreu um erro durante a operação< tente novamente!")
    case 3:
        try:
            num1= int(input("Digite o primeiro numero a ser dividido:"))
            num2= int(input("digite o segundo numero a ser dividido:"))
            divisão = num1+num2
            print(f"a divisão do numero sao {divisão}")
        except:
           print("ocorreu um erro durante a operação< tente novamente!")
    case 4:
        try:
            num1= int(input("Digite o primeiro numero a ser multiplicado:"))
            num2= int(input("digite o segundo numero a ser multiplicado:"))
            multiplicação = num1+num2
            print(f"a multiplicação do numero sao {multiplicação}")
        except:
           print("ocorreu um erro durante a operação< tente novamente!")    



