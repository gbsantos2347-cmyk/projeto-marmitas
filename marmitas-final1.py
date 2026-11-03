
print('___Marmitaria___')

# Gabriel Barreto Santos Araujo - RA: 6002218
# Matheus Henrique de Jesus Bezerra - RA: 6034616 - Relatorio
# Guilherme Batista Mota Costa - RA: 6012701
# Gabriel Vilela Cardoso de Lima - RA: 5979358
# Higor Pereira da Silva - RA: 5979471

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

        # Escolher tamanho da marmita
        tam = input('Tamanho da marmita (P, M, G): ').upper()

        if tam == 'P':
            preco = 15
        elif tam == 'M':
            preco = 18
        elif tam == 'G':
            preco = 22
        else:
            print('Tamanho inválido!')
            continue

        total_mar = qtd * preco

        quantidadeP = 0
        quantidadeM = 0
        quantidadeG = 0

        if tam == 'P':
            quantidadeP = qtd
        elif tam == 'M':
            quantidadeM = qtd
        elif tam == 'G':
            quantidadeG = qtd

        # Distância da entrega
        dis = float(input('Distância da entrega em km: '))

        while dis < 0:
            print('Distância inválida!')
            dis = float(input('Distância da entrega em km: '))

        # Calcular taxa de entrega
        if dis <= 2:
            taxa = 0
            entrega = 'Entrega grátis'

        elif dis <= 5:
            taxa = 5
            entrega = 'Entrega disponível'

        elif dis <= 8:
            taxa = 8
            entrega = 'Entrega disponível'

        else:
            taxa = 0
            entrega = 'Retirada no local (não há entrega)'

        total_fre = total_mar + taxa

        # Atualizar o caixa
        total_caixa += total_fre

        # Registrar pedido no histórico
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
        print('Quantidade de marmitas:', qtd)
        print('Tamanho escolhido:', tam)
        print(f'Valor das marmitas: R$ {total_mar:.2f}')
        print(f'Taxa de entrega: R$ {taxa:.2f}')
        print('Modalidade:', entrega)
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
