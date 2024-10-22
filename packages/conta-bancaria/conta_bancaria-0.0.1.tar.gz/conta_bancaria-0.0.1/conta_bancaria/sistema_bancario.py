# -*- coding: utf-8 -*-
"""2. Desafio Sistema bancario c funcoes.ipynb

"""

from datetime import datetime

def validar_data(data_input):
    try:
        # Tenta converter a string de entrada em um objeto de data
        data = datetime.strptime(data_input, '%d-%m-%Y')
        return data.strftime('%d-%m-%Y')  # Retorna a data formatada corretamente
    except ValueError:
        print("Data inválida. Insira uma data no formato dd-mm-aaaa.")
        return None

#function saque, considering restrictions on the presentation
def saque(*,valor_sacado_no_dia, LIMITE_SAQUE_DIARIO, saldo,contador_saque, extrato,qtde_operacoes,LIMITE_NUMERO_SAQUES):
  while True:
    try:
      valor_saque = float(input('Digite o montante do saque: '))
      if valor_saque >0: #Aceita valores apenas acima de zero, se colocado valor negativo, dá mensagem de erro

        if valor_sacado_no_dia >=LIMITE_SAQUE_DIARIO: #caso limite diário já tenha sido atingito, não permite novo saque
          print ('Limite diário de saque já excedido, não é possivel mais sacar dinheiro hoje. Escolha outra opção no Menu')
          break
        elif saldo <valor_saque: #permite saques apenas se tem saldo na conta
          print (f'Saldo insuficiente, você tem R${saldo:.2f}')
        elif valor_saque + valor_sacado_no_dia >LIMITE_SAQUE_DIARIO: #verifica se valor solicitado somado ao valor já saco no dia irá exceder limite diário
          print (f'Valor a ser sacado excedeu limite diário de R${LIMITE_SAQUE_DIARIO:.2f}')
          break
        elif contador_saque >LIMITE_NUMERO_SAQUES: #limite de quantidade de saques
          print ('Já foi realizado o máximo número de saques, não é possivel executar operação')
          break
        else:
          saldo -=valor_saque
          print(f'Saque no valor de R${valor_saque:.2f} em processo, novo saldo de R${saldo:.2f}')
          contador_saque +=1
          valor_sacado_no_dia +=valor_saque
          qtde_operacoes +=1
          extrato += f"Saque de R${valor_saque:.2f} \n"
          break
      else:
        print ('Valor incorreto, insira um valor valido acima de 0')
    except ValueError:
      print('Entrada inválida. Por favor, insira um número válido.')

  return valor_sacado_no_dia, saldo, contador_saque, extrato, qtde_operacoes

def deposito (saldo, qtde_operacoes,extrato,/):
  valor_depositado = float(input('Digite o valor a ser depositado: '))
  if valor_depositado >0: #Aceita valores apenas acima de zero, se colocado valor negativo, dá mensagem de erro
    saldo +=(valor_depositado)
    qtde_operacoes +=1
    print (f"Valor depositado de R${valor_depositado:.2f}. Novo saldo de R$ {saldo:.2f}" )
    extrato += f"Depósito de R${valor_depositado:.2f} \n"
  else:
    print ('Valor incorreto, insira um valor valido acima de 0')
  return saldo,qtde_operacoes,extrato

def mostra_extrato (qtde_operacoes,saldo,/,*, extrato):
  if qtde_operacoes ==0:
    print ('Não foram realizadas movimentações.')
  else:
    print(f'***EXTRATO*** \nSaldo R${saldo:.2f} \n{extrato}')

def criar_usuario(cadastro): #cpf, nome, endereco e data de nascimento'
  while True:
    cpf = input('CPF - apenas números sem traços ou pontos: (Caso deseje sair, digite s) ')
    if cpf in cadastro:
      print('CPF / Usuário já existente, insira outro CPF. ')
    elif cpf.lower() == 's':
      break
    else:
      nome = input ('Insira nome completo: ')
      endereco = input ('Insira endereco (Logradouro, nro, bairro, cidade/estado(sigla): ' )
      data_nascimento = input('Insira data de nascimento: (dd-mm-aaaa')

      data_valida = None

      while data_valida is None:
        data_valida = validar_data(data_nascimento)
        if data_valida is None:  # Se a data não for válida, solicita novamente
          data_nascimento = input("Data de nascimento: (dd-mm-aaaa): ")

      cadastro[cpf] = {'nome': nome, 'endereco': endereco, 'data_nascimento':data_nascimento}
      print(f"CPF Cadastrado: {cpf}")
      print(f"Nome : {cadastro [cpf] ['nome']}")
      print(f"Endereço : {cadastro [cpf] ['endereco']}")
      print(f"Data de nascimento: {cadastro[cpf]['data_nascimento']} ")
      break

  return cadastro

def criar_conta_corrente (cadastro, conta_corrente):
  while True:
    cpf = input('Informe o cpf do usuário. (Aperte s para sair)')
    if cpf.lower() == 's': #caso usuario digite "S" (maiusculo), aceita como opção para sair
      break
    else:
      if cpf in cadastro: #caso CPF, existe, cadastra, se não existir, dá mensagem de erro
        numero_conta = len(conta_corrente) +1
        conta_corrente[numero_conta] = {
            'cpf': cpf,
            'agencia' : '0001',

        }
        print (f"Conta cadastrada. Usuário {cpf}, agencia: {conta_corrente[numero_conta]['agencia']}, conta corrente:{numero_conta} ")
        break
      else:
        print('Usuário não cadastrado. Informe um usuário cadastrado ou cadastre um novo usuário')
  return conta_corrente

def exibir_cadastro(cadastro, conta_corrente):
  print("="*50 ,'\n\033[1mCadastros de usuário:\033[0m')
  for cpf, dados in cadastro.items():
    print(f"CPF: {cpf}, Nome: {dados['nome']}, Data de Nascimento: {dados['data_nascimento']}" )
  print('\n', "="*50, '\n\033[1mCadastros de contas:\033[0m')
  for numero_conta,conta in conta_corrente.items():
    print (f"Número da conta {numero_conta} , CPF: {conta['cpf']}, agencia: {conta['agencia']}, nome: {cadastro[conta['cpf']]['nome']  } ")

def realizar_operacao():
  
  #constants

  LIMITE_SAQUE_DIARIO = float(500.00)
  LIMITE_NUMERO_SAQUES= int(3)

  MENU= '''
  Digite a opção desejada
  [1] Saque
  [2] Depósito
  [3] Extrato
  [4] Criar usuário
  [5] Criar conta-corrente
  [6] Sair
  [7] Mostrar contas e usuários cadastrados
  '''

  #Variables
  saldo = float(1200.00)
  valor_sacado_no_dia = 0
  qtde_operacoes =0
  valor_depositado = int(0)
  contador_saque=int(1)
  extrato =''
  conta_corrente = {}
  cadastro = {}
  #sistema bancário
  while True:
    opcao = input(MENU)
    if opcao=='1':
      valor_sacado_no_dia, saldo, contador_saque, extrato, qtde_operacoes = saque(valor_sacado_no_dia=valor_sacado_no_dia , LIMITE_SAQUE_DIARIO=LIMITE_SAQUE_DIARIO, saldo=saldo,
                                                                                  contador_saque=contador_saque, extrato=extrato,qtde_operacoes=qtde_operacoes, LIMITE_NUMERO_SAQUES= LIMITE_NUMERO_SAQUES)
    elif opcao=='2':
      saldo,qtde_operacoes,extrato = deposito (saldo,qtde_operacoes,extrato)

    elif opcao=='3':
      mostra_extrato (qtde_operacoes,saldo, extrato=extrato)
    elif opcao == '4':
      cadastro = criar_usuario (cadastro)
    elif opcao =='5':
      conta_corrente = criar_conta_corrente(cadastro,conta_corrente)
    elif opcao =='6':
      break
    elif opcao =='7':
      exibir_cadastro(cadastro, conta_corrente)
    else:
      print('Opção incorreta, digite novamente')
  print('Obrigado por usar nossos serviços')