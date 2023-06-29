import os
menu = """==========Selecione uma Opção==========

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE_VALOR_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_QUANTIDADE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        os.system('cls')
        deposito = input("Digite o valor que você deseja depositar: ")
        try:
            if float(deposito) < 0:
                print('Você não pode depositar um valor negativo')
                continue
            else:
                saldo += float(deposito)
        except:
            print('Você não digitou um valor válido')
            continue
        extrato += f'Depósito: R$ {float(deposito):.2f} \n'
    elif opcao == 's':
        os.system('cls')
        if saldo > 0:
            if numero_saques < LIMITE_QUANTIDADE_SAQUES:
                saque = input('Digite o valor do seu saque: ')
                try:
                    saque = float(saque)
                    if saque < 0:
                        print('Você não digitou um valor válido')
                        continue
                    if saque < LIMITE_VALOR_SAQUE:
                        if saque < saldo:
                            saldo -= saque
                            extrato += f'Saque: R$ {saque:.2f}\n'
                        else:
                            print('Você não possui saldo suficiente para realizar esse saque')
                            continue
                    else:
                        print('Você ultrapassou o limite de saque.')
                        continue
                except:
                    print('Você não digitou um valor válido')
                    continue
                numero_saques += 1
            else:
                print('Você ultrapassou o número de saques diários')
        else:
            print('Você não possui saldo!')
    elif opcao == 'e':
        os.system('cls')
        print(extrato, end='')
        print(f'Saldo: R$ {saldo:.2f}')
    elif opcao == 'q':
        os.system('cls')
        break
    else:
        os.system('cls')
        print('Operação inválida, por favor selecione novamente a operação desejada.')

