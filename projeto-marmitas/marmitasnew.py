
print('___Marmitaria___')

total_caixa = 0 

while True:
    print('Opção 1 - Registrar Pedido') # Gabriel Barreto Santos Araujo RA: 6002218
    print('Opção 2 - Fechar o dia') # Gabriel Barreto Santos Araujo RA: 6002218
    print('Opção 0 - Desligar programa') # Gabriel Barreto Santos Araujo RA: 6002218

    opcao = input('Escolha uma das opções: ') # Gabriel Barreto Santos Araujo RA: 6002218

    if opcao == '1': # Gabriel Barreto Santos Araujo RA: 6002218
        qtd = int(input('Quantidade de marmitas? ')) 

        while qtd <= 0 or qtd >= 11:
            print('Quantidade inválida')
            qtd = int(input('Quantidade de marmitas? '))

        tam = input('Tamanho da marmita (P, M, G): ')

        if tam == 'P':
            preco = 15
        elif tam == 'M':
            preco = 18
        elif tam == 'G':
            preco = 22
        else:
            print('Tamanho inválido')
            continue

        total_mar = qtd * preco # Gabriel Barreto Santos Araujo RA: 6002218

        dis = float(input('Distância da entrega em km: '))

        if dis < 0:
            print('Distância inválida')
            continue

        if dis <= 2 or total_mar >= 80:
            taxa = 0
        elif dis <= 5:
            taxa = 5
        elif dis <= 8:
            taxa = 8
        else:
            print('Pedido para retirada no local')
            taxa = 0

        total_fre = total_mar + taxa # Gabriel Barreto Santos Araujo RA: 6002218
        total_caixa += total_fre 

        print('--- RESUMO DO PEDIDO ---')
        print('Valor das marmitas: R$', total_mar) # Gabriel Barreto Santos Araujo RA: 6002218
        print('Valor da entrega: R$', taxa) # Gabriel Barreto Santos Araujo RA: 6002218
        print('Total do pedido: R$', total_fre)# Gabriel Barreto Santos Araujo RA: 6002218 

    elif opcao == 2:
        print('Fechamento do dia')

    elif opcao == '0':
        print('Programa encerrado')
        break

    else:
        print('Opção inválida!')
