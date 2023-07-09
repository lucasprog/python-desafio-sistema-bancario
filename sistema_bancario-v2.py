import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print(""" 
  =====================================================
    Olá Bem vindo ao banco TesTCoin
    Para iniciarmos informe seu dados para se cadastrar
  =====================================================
  """)

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

nome = ""
data_nasc = ""
cpf = 0
endereco = ""
usuarios = []

def alertMensagem(mensagem):
  print(f'\n**ALERT**! {mensagem} \n')

def existe(listValor, chaveValor, comparador):
  existe = False  
  for valor in listValor:
    if valor[chaveValor] == comparador:
      existe = True
  
  return existe

#Function Extrato
def _extrato(extrato,saldo):
  print(extrato)
  print("---------------------------------------")
  print(f"Valor Total: R$ {locale.currency(saldo,grouping=True,symbol=None)}")

# Function Depositar
def _depositar(valorDeposito):
  saldo = 0
  extrato = ''

  if valorDeposito < 1:
    alertMensagem("Valor inválido")
    return False
  else:
    saldo = valorDeposito
    extrato = f"--- Deposito no valor R$ {locale.currency(valorDeposito,grouping=True,symbol=None)}\n"
    return dict(saldo=saldo,extrato=extrato)

#Function Sacar
def _sacar(valorSaque, saldo, extrato):
  
  if valorSaque < 1:
      print('Valor inválido')
      return False
  else:

    if saldo > 0:
      if valorSaque <= saldo:
        saldo -= valorSaque
        extrato += f"--- Saque no valor R$ {locale.currency(valorSaque,grouping=True,symbol=None)}\n"          
        return dict(saldo=saldo,extrato=extrato)          
      
      else:
        alertMensagem("Valor insuficiente, no momento seu saldo é de  R$ {locale.currency(saldo,grouping=True,symbol=None)}")
        return False
    else:
      alertMensagem("Saldo insuficiente.")      
      return False

while True:

  usuario = ""
  usuarioChave = 0

  if( len(usuarios) > 0):
    messageEscolhaUsuario = "Selecionar Usuário::\n\n"

    for (indice, usuario) in enumerate(usuarios):
      messageEscolhaUsuario += f"{usuario[0]} - Digite {indice} \n"

    messageEscolhaUsuario += "\nPara ir para próxima opção digite (O):: "

    selecionarUsuario = input(messageEscolhaUsuario)

    if selecionarUsuario == "O":
      novoUsuario = input("\nDeseja cadastrar novo usuário?(S/N):: ")     
    else:
      usuarioChave = int(selecionarUsuario)
      usuario = usuarios[usuarioChave]
      novoUsuario = "N"

  else:
    novoUsuario = 'S'

  if novoUsuario == 'S':
    nome = input("Digite seu nome: ")
    data_nasc = input("Digite sua Data de nascimento: ")  
    cpf = int(input("Digite seu CPF: "))
    endereco = input("Digite seu Endereço: ")
    
    if existe(usuarios,2,cpf):
      alertMensagem("Usuário com esse CPF já existe")
      continue
    
    usuarios.append([nome,data_nasc,cpf,endereco,[]])  
    usuario = usuarios[-1]
    usuarioChave = len(usuarios) - 1

  if len(usuario[4]) > 0:
    novaConta = input("\nDeseja cadastrar uma nova conta?(S/N):: ")
  else:
    novaConta = 'S'

  if novaConta == 'S':
    contaCadastrada = True
    while contaCadastrada:
      agencia = input("Digite o número da agência: ")
      conta = input("Digite o número da conta: ")

      for indice,usuarioInLoop in enumerate(usuarios):
        if existe(usuarioInLoop[-1],0,agencia) or existe(usuarioInLoop[-1],1,conta):
          alertMensagem('Conta já cadastrada, por favor informe outra!')
        else:
          usuarios[usuarioChave][-1].append([agencia,conta])
          continuar = input('Deseja cadastrar outra conta?(S/N)::')
          if continuar == 'N':
            contaCadastrada = False
          break

  #Question about the option user want to do
  opcao = float(input(menu))

  if opcao == 1:
    valorDeposito = float(input("Digite o valor a ser depositado:"))
    deposito = _depositar(valorDeposito)

    if not deposito:
      continue
      
    saldo = deposito['saldo']
    extrato = deposito['extrato']
    
  elif opcao == 2:
    valorSaque = float(input("Digite o valor a ser sacado:"))
    
    if saque_vezes < limite_saque_vezes:
      if valorSaque <= LIMITE_SAQUE:
        saque = _sacar(valorSaque=valorSaque, saldo=saldo, extrato=extrato)
        
        if not saque:
          continue   
        
        saldo = saque['saldo']
        extrato = saque['extrato']

      else:
        print(f'Limite de saque é de R$ {locale.currency(LIMITE_SAQUE,grouping=True, symbol=None)}')
        continue
    else:
      print("Você chegou no limite de saque diário")  
      continue
  

    saque_vezes += 1

  elif opcao == 0:
    print('Operação encerrada')
    break

  elif opcao == 3:  
    _extrato(extrato,saldo=saldo)