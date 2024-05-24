import random
from datetime import datetime

### DADOS DO USUÁRIO
nome_usuario = 'Matheus Eleutério'
cpf_usuario = '46639354861'  # apenas números
senha_usuario = '102030'  # limitado a 6 números

### SALDO NAS CARTEIRAS
saldos = {
    'Real': 0, 
    'Bitcoin': 0, 
    'Ethereum': 0, 
    'Ripple': 0
    }

### COTAÇÃO BASE DA MOEDA
cotacao = {
    'Bitcoin': 358017.09, 
    'Ethereum': 19444.23, 
    'Ripple': 2.72
    }

### TAXA DE COMPRA
taxa_compra = {
    'Bitcoin': 1.02,    
    'Ethereum': 1.01, 
    'Ripple': 1.01
    }

### TAXA DE VENDA
taxa_venda = {
    'Bitcoin': 1.03, 
    'Ethereum': 1.02, 
    'Ripple': 1.01
    }

### HISTORICO DE OPERAÇÕES PARA EXIBIR NO ARQUIVO .TXT
historico_operacoes = []

################################################################################################################
def login_usuario():
    print("\n########## Exchange de Criptomoedas ##########\n")
    print("Entre com seus dados abaixo para fazer login:")

    while True:
        cpf_digitado = input("Digite seu CPF (Apenas números): ")
        senha_digitada = input("Digite sua senha: ")

        if cpf_digitado == cpf_usuario and senha_digitada == senha_usuario:
            print("Login efetuado com sucesso!")
            return True
        else:
            print("CPF ou senha incorretos. Verifique os dados digitados!\n")


################################################################################################################
def menu_principal():
    print("\n#### Menu de opções #### ")
    print("1. Consultar saldo")
    print("2. Consultar extrato")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Comprar criptomoedas")
    print("6. Vender criptomoedas")
    print("7. Atualizar cotação")
    print("0. Sair")


################################################################################################################
def consultar_saldo():
    print("Você selecionou a opção de consultar saldo.")
    senha_digitada_fsaldo = input("\nDigite sua senha: ")

    if senha_digitada_fsaldo == senha_usuario:
        cpf_formatado = f"{cpf_usuario[:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:]}"  #formatação do cpf com pontos e traços
        print("\nSaldo na carteira:")
        print("\nNome:", nome_usuario)
        print("CPF:", cpf_formatado)
        print(f"Saldo Real: R$ {saldos['Real']:.2f}")
        print(f"Saldo Bitcoin: BTC {saldos['Bitcoin']:.6f}")
        print(f"Saldo Ethereum: ETH {saldos['Ethereum']:.6f}")
        print(f"Saldo Ripple: XRP {saldos['Ripple']:.6f}")
        input(f"\nPressione ENTER para voltar ao menu de opções do usuário: ")
    else:
        print("Senha incorreta. Verifique a senha digitada.")

################################################################################################################
def depositar():
    print("Você selecionou a opção de depositar reais na carteira.")
    deposito = float(input("\nDigite o valor a ser depositado: "))

    if deposito > 0:
        saldos['Real'] += deposito  

        descricao = f"Depósito recebido no valor de R$ {deposito:.2f}"
        data_hora, descricao = operacao('+', deposito, 'Real', 1.0, 0.0, saldos)
        historico_operacoes.append((data_hora, descricao))

        print("\nOperação realizada com sucesso! Consulte seus saldos atualizados: ")
        print("\nSaldo disponível na carteira:")
        print(f"Real: R$ {saldos['Real']:.2f}")
        print(f"Bitcoin: BTC {saldos['Bitcoin']:.6f}")
        print(f"Ethereum: ETH {saldos['Ethereum']:.6f}")
        print(f"Ripple: XRP {saldos['Ripple']:.6f}")
        salvar()
        input(f"\nPressione ENTER para retornar ao menu de opções do usuário:")
    else:
        print("Erro ao realizar a operação. Verifique se o valor digitado é um valor válido.")
    salvar()

################################################################################################################
def sacar(): 
    print("Você selecionou a opção de sacar saldo da carteira.")
    saque = float(input("\nDigite o valor que deseja sacar: "))

    if saque <= saldos['Real']:
        saldos['Real'] -= saque

        descricao = f"Saque efetuado no valor de R$ {saque:.2f}"
        data_hora, descricao = operacao('-', saque, 'Real', 1.0, 0.0, saldos)
        historico_operacoes.append((data_hora, descricao))

        print("\nOperação realizada com sucesso! Consulte seus saldos atualizados: ")
        print("\nSaldo disponível na carteira:")
        print(f"Real: R$ {saldos['Real']:.2f}")
        print(f"Bitcoin: BTC {saldos['Bitcoin']:.6f}")
        print(f"Ethereum: ETH {saldos['Ethereum']:.6f}")
        print(f"Ripple: XRP {saldos['Ripple']:.6f}")
        salvar()
        input(f"\nPressione ENTER para retornar ao menu de opções do usuário:")
    else:
        print("\nVocê não possui saldo suficiente para realizar esta operação.")
        input("\nPressione ENTER para retornar ao menu de opções do usuário: ")

#################################################################################################################
def comprar():
    print("Você selecionou a opção de comprar criptomoedas.")  # fcompra = função comprar
    senha_digitada_fcomprar = input("\nDigite sua senha: ")

    if senha_digitada_fcomprar == senha_usuario:
        print("\n### Consulte as cotações atualizadas ###")
        print(f"Bitcoin (BTC):  Cotado em R$ {cotacao['Bitcoin']:.6f}")
        print(f"Ethereum (ETH): Cotado em R$ {cotacao['Ethereum']:.6f}")
        print(f"Ripple (XRP):   Cotado em R$ {cotacao['Ripple']:.6f}")

        tipo_criptomoeda = input("\nInforme qual criptomoeda você deseja comprar: ")
        qtd_moedas = float(input("Informe a quantidade que deseja comprar: "))

        if tipo_criptomoeda in cotacao:  ##verifica moeda valida
            cotacao_atual = cotacao[tipo_criptomoeda]
            valor_compra = cotacao_atual * qtd_moedas
            valor_final = valor_compra * taxa_compra[tipo_criptomoeda]  ##taxa de op

            print(f"\nValor total da compra: R${valor_final:.2f}")
            resposta = input("Deseja finalizar a compra? (s/n): ")
            if resposta == 's':
                if valor_final <= saldos['Real']:  # verifica e atualiza o saldo disponível
                    saldos['Real'] -= valor_final
                    saldos[tipo_criptomoeda] += qtd_moedas

                    descricao = f"Compra de {qtd_moedas} {tipo_criptomoeda} no valor total de R$ {valor_final:.2f}"
                    data_hora, descricao = operacao('Compra', valor_final, tipo_criptomoeda, cotacao_atual, taxa_compra[tipo_criptomoeda], saldos)
                    historico_operacoes.append((data_hora, descricao))

                    print("\nOperação realizada com sucesso! Consulte seus saldos atualizados: ")
                    print("\nSaldo disponível na carteira:")
                    print(f"Real: R$ {saldos['Real']:.2f}")
                    print(f"Bitcoin: BTC {saldos['Bitcoin']:.6f}")
                    print(f"Ethereum: ETH {saldos['Ethereum']:.6f}")
                    print(f"Ripple: XRP {saldos['Ripple']:.6f}")
                    salvar()
                    input(f"\nPressione ENTER para retornar ao menu de opções do usuário: ")
                else:
                    print("Você não possui saldo suficiente para realizar esta operação.")
                    input(f"\nPressione ENTER para retornar ao menu de opções do usuário: ")
            else:
                print("Compra cancelada.")
        else:
            print("Criptomoeda não encontrada. Selecione uma opção válida.")  # tratando possíveis erros
    else:
        print("Senha incorreta. Verifique a senha digitada.")
################################################################################################################
def vender():
    print("Você selecionou a opção de vender criptomoedas.")  # fvenda = função vender
    senha_digitada_fvender = input("\nDigite sua senha: ")

    if senha_digitada_fvender == senha_usuario:
        print("\n### Consulte as cotações atualizadas ###")
        print(f"Bitcoin (BTC):  Cotado em R$ {cotacao['Bitcoin']:.6f}")
        print(f"Ethereum (ETH): Cotado em R$ {cotacao['Ethereum']:.6f}")
        print(f"Ripple (XRP):   Cotado em R$ {cotacao['Ripple']:.6f}")

        tipo_criptomoeda = input("\nInforme qual criptomoeda você deseja vender: ")
        qtd_moedas = float(input("Informe a quantidade que deseja vender: "))

        if tipo_criptomoeda in cotacao:  ##verifica moeda valida
            cotacao_atual = cotacao[tipo_criptomoeda]
            valor_venda = cotacao_atual * qtd_moedas
            valor_final = valor_venda * taxa_venda[tipo_criptomoeda]  ##taxa de op

            print(f"\nValor total da venda: R${valor_final:.2f}")
            resposta = input("Deseja finalizar a venda? (s/n): ")
            if resposta == 's':
                if qtd_moedas <= saldos[tipo_criptomoeda]:
                    saldos['Real'] += (valor_venda * (2 - taxa_venda[tipo_criptomoeda]))  # 2 porque o valor da taxa possui o 1.xx"
                    saldos[tipo_criptomoeda] -= qtd_moedas

                    descricao = f"Venda de {qtd_moedas} {tipo_criptomoeda} no valor de R$ {valor_final:.2f}"
                    data_hora, descricao = operacao('Venda', valor_final, tipo_criptomoeda, cotacao_atual, taxa_venda[tipo_criptomoeda], saldos)
                    historico_operacoes.append((data_hora, descricao))

                    print("\nOperação realizada com sucesso! Consulte seus saldos atualizados: ")
                    print("\nSaldo disponível na carteira:")
                    print(f"Real: R$ {saldos['Real']:.2f}")
                    print(f"Bitcoin: BTC {saldos['Bitcoin']:.6f}")
                    print(f"Ethereum: ETH {saldos['Ethereum']:.6f}")
                    print(f"Ripple: XRP {saldos['Ripple']:.6f}")
                    salvar()
                    input(f"\nPressione ENTER para retornar ao menu de opções do usuário: ")
                else:
                    print("Você não possui saldo suficiente para realizar esta operação.")
                    input(f"\nPressione ENTER para retornar ao menu de opções do usuário: ")
            else:
                print("Venda cancelada.")
        else:
            print("Criptomoeda não encontrada. Selecione uma opção válida.")  # tratando possíveis erros
    else:
        print("Senha incorreta. Verifique a senha digitada.")



#################################################################################################################
def atualizar():
    variacao = {'max': 1.05, 'min': 0.95}

    for tipo_criptomoeda, cotacao_atual in cotacao.items():
        variacao_atual = random.uniform(variacao['min'], variacao['max'])
        cotacao_atualizada = cotacao_atual * variacao_atual
        cotacao[tipo_criptomoeda] = round(cotacao_atualizada, 6)

    print("Cotações atualizadas com sucesso!")
    print("\n### Consulte as cotações atualizadas ###")
    print(f"Bitcoin (BTC):  Cotado em R$ {cotacao['Bitcoin']:.6f}")
    print(f"Ethereum (ETH): Cotado em R$ {cotacao['Ethereum']:.6f}")
    print(f"Ripple (XRP):   Cotado em R$ {cotacao['Ripple']:.6f}")

#################################################################################################################
def consultar_extrato():
    print("Você selecionou a opção de consultar extrato.")
    senha_digitada_fextrato = input("\nDigite sua senha: ")

    if senha_digitada_fextrato == senha_usuario:
        cpf_formatado = f"{cpf_usuario[:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:]}"  # Formatação do CPF com pontos e traços
        print("\nExtrato da conta:")
        print("\nNome:", nome_usuario)
        print("CPF:", cpf_formatado)
        print("\nOperações:")

        if 'Extrato' in saldos:
            for operacao in saldos['Extrato']:
                data_hora, tipo, valor, moeda, cotacao, taxa, saldos_atualizados = operacao
                data_formatada = data_hora.strftime("%d-%m-%Y %H:%M:%S")
                saldo_real, saldo_bitcoin, saldo_ethereum, saldo_ripple = saldos_atualizados.values()
                print(f"{data_formatada} | {'+' if tipo == 'Depósito' or tipo == 'Compra' else '-'} {valor:.2f} {moeda} | CT: {cotacao:.6f} | TX: {taxa:.2f} | REAL: {saldo_real:.2f} | BTC: {saldo_bitcoin:.6f} | ETH: {saldo_ethereum:.6f} | XRP: {saldo_ripple:.6f}")
        else:
            print("Nenhuma operação registrada ainda.")

        input("\nPressione ENTER para retornar ao menu de opções do usuário: ")
    else:
        print("Senha incorreta. Verifique a senha digitada.")



################################################ FUNÇÕES AUXILIARES #############################################
def salvar():
    with open('dados_usuario.txt', 'w') as f:
        f.write("### Dados do usuário ###\n")
        f.write(f"Nome: {nome_usuario}\n")
        f.write(f"CPF: {cpf_usuario}\n")
        f.write(f"Senha: {senha_usuario}\n\n")
        f.write("## Saldo na carteira:\n")
        for moeda, saldo in saldos.items():
            f.write(f"{moeda}: {saldo}\n")
        f.write("\n## Histórico de operações:\n")
        for operacao in historico_operacoes:
            f.write(f"{operacao[1]}\n")

#################################################################################################################
def operacao(tipo, valor, moeda, cotacao, taxa, saldos):
    now = datetime.now()
    data_hora = now.strftime("%d/%m/%Y %H:%M:%S")
    descricao = None
    if tipo == '+':
        descricao = f"{data_hora} - Depósito recebido no valor de {valor:.2f} reais"
    elif tipo == '-':
        descricao = f"{data_hora} - Saque efetuado no valor de {valor:.2f} reais"
    elif tipo == 'Compra':
        descricao = f"{data_hora} - Compra de {moeda} no valor total de {valor:.2f} reais"
    elif tipo == 'Venda':
        descricao = f"{data_hora} - Venda de {moeda} no valor de {valor:.2f} reais"
    return data_hora, descricao


################################################################################################################
