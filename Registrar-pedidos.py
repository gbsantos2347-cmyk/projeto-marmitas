# Gabriel Vilela Cardoso de Lima


marmitaP = 15.00

marmitaM = 18.00

marmitaG = 22.00


while True:
    print("Opção 1 - Registrar Pedido")
    print("Opção 2 - Fechar o dia")
    opcao = input("Escolha uma das Opções? ")

    if opcao == '1':
        qtd = int(input("Quantidade de Marmitas? "))
        while qtd <= 0 or qtd >= 11:
            print("Quantidade invalida")
            qtd = int(input("Quantidades de Marmitas? "))
        total_mar = 0

        for s in range(qtd):
            tam = input(f"Tamanho da Marmita {s+1}: P,M,G: ").upper()
            while tam not in ['P', 'M', 'G']:
                print("Opção inválida!")
                tam = input(f"Tamanho da Marmita {s+1}: P,M,G: ").upper()

            if tam == 'P':
                total_mar += marmitaP
            elif tam == 'M':
                total_mar += marmitaM
            elif tam == 'G':
                total_mar += marmitaG
        print(total_mar)

    elif opcao == '2':
        print("Encerrando Atendimento")
        break
    else:
        print("Mensagem invalida!")