import functions

def main():
    if functions.login_usuario():
        while True:
            functions.menu_principal()
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                functions.consultar_saldo()
            elif opcao == '2':
                functions.consultar_extrato()
            elif opcao == '3':
                functions.depositar()
            elif opcao == '4':
                functions.sacar()
            elif opcao == '5':
                functions.comprar()
            elif opcao == '6':
                functions.vender()
            elif opcao == '7':
                functions.atualizar()
            elif opcao == '0':
                print("Você saiu do programa!")
                break
            else:
                print("Opção inválida! Verifique a opção selecionada.")
main()
