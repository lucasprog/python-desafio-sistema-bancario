import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

menu = """
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair
"""

saldo = 0
extrato = "--------------------\n*** EXTRATO *** \n\n"
limite_saque_vezes = 3
saque_vezes = 0
LIMITE_SAQUE = 500

while True:

  opcao = float(input(menu))

  if opcao == 1:
    valorDeposito = float(input("Digite o valor a ser depositado:"))
    
    if valorDeposito < 1:
        print('Valor inválido')
        continue
    else:
      saldo += valorDeposito
      extrato += f"--- Deposito no valor R$ {locale.currency(valorDeposito,grouping=True,symbol=None)}\n"

  elif opcao == 2:

    valorSaque = float(input("Digite o valor a ser sacado:"))

    if valorSaque < 1:
        print('Valor inválido')
        continue
    else:

      if saldo > 0:

        if valorSaque <= saldo:

          if saque_vezes < limite_saque_vezes:

            if valorSaque <= LIMITE_SAQUE:

              saldo -= valorSaque
              extrato += f"--- Saque no valor R$ {locale.currency(valorSaque,grouping=True,symbol=None)}\n"
              saque_vezes += 1

            else:
              print(f'Limite de saque é de R$ {locale.currency(LIMITE_SAQUE,grouping=True, symbol=None)}')
              continue

          else:
            print("Você chegou no limite de saque diário")
            continue

        else:
          print(f'Valor insuficiente, no momento seu saldo é de  R$ {locale.currency(saldo,grouping=True,symbol=None)}')
          continue

      else:
        print('Saldo insuficiente.')      
        continue

  elif opcao == 0:
    print('Operação encerrada')
    break

  elif opcao == 3:  
    print(extrato)
    print("---------------------------------------")
    print(f"Valor Total: R$ {locale.currency(saldo,grouping=True,symbol=None)}")
   
