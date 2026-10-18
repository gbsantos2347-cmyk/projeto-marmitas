
# Matheus Henrique de Jesus Bezerra - 6034616 - responsavel pelo "relatorio"


print('___Marmitaria___')

total_caixa = 0 
#esse é o relatorio que vai armazenar os pedidos
relatorio = [] 

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

            #aqui eu estou adicionando os dados do pedido no relatorio
            relatorio.append([tam, qtd, preco, total_mar, taxa, total_fre])
        
        print('--- RESUMO DO PEDIDO ---')
        print('Valor das marmitas: R$', total_mar) # Gabriel Barreto Santos Araujo RA: 6002218
        print('Valor da entrega: R$', taxa) # Gabriel Barreto Santos Araujo RA: 6002218
        print('Total do pedido: R$', total_fre)# Gabriel Barreto Santos Araujo RA: 6002218 

        #aqui esta somando a quantidade de pedidos realizados e imprimindo na tela
        qtd_pedidos = len(relatorio)
        print('Quantidade de pedidos realizados: ', qtd_pedidos) 


    
    elif opcao == 2:
        print('Fechamento do dia')

    elif opcao == '0':
        print('Programa encerrado')

        #Essa e a parte que soma a quantidade de marmitas vendidas por tamanho e imprime na tela
        total_p = 0
        total_M = 0
        total_G = 0
        
        # Aqui esta o codigo da conta e como que funciona a soma das marmitas vendidas por tamanho, e o total de marmitas
        for pedido in relatorio:
            if pedido[0] == 'P':
                total_p = total_p + pedido[1]

            elif pedido[0] == 'M':
                total_M = total_M + pedido[1]

            elif pedido[0] == 'G':
                total_G = total_G + pedido[1]
        
        #Aqui e a parte que imprime na tela a quantidade de marmitas vendidas por tamanho e o total de marmitas vendidas
        print('\n--- RELATÓRIO DOS PEDIDOS ---')
        print('Marmitas P - R$ 15,00 vendidas: ', total_p)
        print('Marmitas M - R$ 18,00 vendidas: ', total_M)

        print('Marmitas G - R$ 22,00 vendidas: ', total_G)

        print('total de pedidos realizados: ', len(relatorio))

        print("total de marmitas vendidas: ", total_p + total_M + total_G)

        if len(relatorio) > 0:
            media = total_mar / len(relatorio)
        else:
            media = 0   

        print(f"Média de valores por pedido: {media:.2f}")

        total_taxa = 0
        for pedido in relatorio:
            total_taxa += pedido[4]  # Adiciona o valor da taxa de cada pedido

        print("Total de taxas: R$ ", total_taxa)


        total_vendas = 0
        for pedido in relatorio:
            total_vendas += pedido[5]  # Adiciona o valor total de cada pedido

        print("Total de vendas: R$ ", total_vendas)
        
        break

    else:
        print('Opção inválida!')
