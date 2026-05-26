import os 

sentinela = 1

while (sentinela == 1): 
    print("*******************")
    print("1 - para Adição: ")
    print("2 - para Subtração: ")
    print("3 - para Multiplicação: ")
    print("4 - para Divisão: ")
    print("*********************")

    operacao = input("EScolha a operação: ")
    valor1 = input("Digite o primeiro número: ")
    valor2 = input("Digite o segudo número: ")
    
    operacao = int(operacao)
    valor1 = float(valor1)
    valor2 = float(valor2)

    if(operacao == 1):
        resultado = valor1 + valor2
    elif(operacao == 2):
        resultado = valor1 - valor2    
    elif(operacao == 3):
        resultado = valor1 * valor2
    elif(operacao == 4):
        resultado = valor1 / valor2
    else:
        resultado = 0
        print("Operação não informada corretamente")  

    print("O resultado do cálculo é: ", resultado)

    print("****************************")
    print("Deseja continuar?")
    print(" 1 - SIM")
    print("2 - NÃO")
    sentinela = int(input("informe a opção: "))
    os.system("cls")