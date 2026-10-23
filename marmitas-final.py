
print('___Marmitaria___')

# Gabriel Barreto Santos Araujo - RA: 6002218

marmitaP = 15
marmitaM = 18
marmitaG = 22

total_caixa = 0
relatorio = []

while True:
    print('\nOpção 1 - Registrar Pedido')
    print('Opção 2 - Fechar o dia')
    print('Opção 0 - Desligar programa')

    opcao = input('Escolha uma das opções: ')

    # Registrar pedido
    if opcao == '1':
        qtd = int(input('Quantidade de marmitas? '))

        while qtd <= 0 or qtd >= 11:
            print('Quantidade inválida!')
            qtd = int(input('Quantidade de marmitas? '))

        total_mar = 0
        quantidadeP = 0
        quantidadeM = 0
        quantidadeG = 0

        # Escolher o tamanho de cada marmita
        for s in range(qtd):
            tam = input(
                f'Tamanho da marmita {s + 1} (P, M, G): '
            ).upper()

            while tam not in ['P', 'M', 'G']:
                print('Tamanho inválido!')
                tam = input(
                    f'Tamanho da marmita {s + 1} (P, M, G): '
                ).upper()

            if tam == 'P':
                total_mar += marmitaP
                quantidadeP += 1

            elif tam == 'M':
                total_mar += marmitaM
                quantidadeM += 1

            elif tam == 'G':
                total_mar += marmitaG
                quantidadeG += 1

        # Distância da entrega
        dis = float(input('Distância da entrega em km: '))

        while dis < 0:
            print('Distância inválida!')
            dis = float(input('Distância da entrega em km: '))

        # Calcular taxa de entrega
        if dis <= 2 or total_mar >= 80:
            taxa = 0

        elif dis <= 5:
            taxa = 5

        elif dis <= 8:
            taxa = 8

        else:
            print('Pedido para retirada no local.')
            taxa = 0

        total_fre = total_mar + taxa

        # Atualizar o caixa
        total_caixa += total_fre

        # Registrar o pedido no histórico
        pedido = {
            'P': quantidadeP,
            'M': quantidadeM,
            'G': quantidadeG,
            'valor_marmitas': total_mar,
            'taxa': taxa,
            'total': total_fre,
            'distancia': dis
        }

        relatorio.append(pedido)

        # Mostrar resumo do pedido
        print('\n--- RESUMO DO PEDIDO ---')
        print('Marmitas P:', quantidadeP)
        print('Marmitas M:', quantidadeM)
        print('Marmitas G:', quantidadeG)
        print(f'Valor das marmitas: R$ {total_mar:.2f}')
        print(f'Taxa de entrega: R$ {taxa:.2f}')
        print(f'Total do pedido: R$ {total_fre:.2f}')

    # Fechamento do dia
    elif opcao == '2':
        print('\n--- FECHAMENTO DO DIA ---')

        totalP = 0
        totalM = 0
        totalG = 0
        total_vendas = 0

        for pedido in relatorio:
            totalP += pedido['P']
            totalM += pedido['M']
            totalG += pedido['G']
            total_vendas += pedido['total']

        print('Quantidade vendida de P:', totalP)
        print('Quantidade vendida de M:', totalM)
        print('Quantidade vendida de G:', totalG)
        print('Total de pedidos:', len(relatorio))
        print(f'Faturamento dos pedidos: R$ {total_vendas:.2f}')
        print(f'Total em caixa: R$ {total_caixa:.2f}')

    # Encerrar programa
    elif opcao == '0':
        print('Programa encerrado!')
        break

    else:
        print('Opção inválida!')
