print('___Marmitaria___')

opcao = -1

while opcao != 0:
    print('1- Registrar pedido')
    print('2- Fechamento de caixa')
    print('0- Desligar programa')

    opcao = int(input('Escolha uma das opções: '))

    if opcao == 1:
        qtd = int(input('Quantidade de marmitas: '))

        if qtd <= 0:
            print('Quantidade inválida')
        elif qtd > 10:
            print('Quantidade excedida')
        else:
            tam = input('Tamanho da marmita (P, M, G): ')

            if tam == 'P':
                preco = 15
            elif tam == 'M':
                preco = 18
            elif tam == 'G':
                preco = 22
            else:
                print('Tamanho inválido')
                preco = 0
            
                

            total_mar = qtd * preco

            

            dis = float(input('Distância da entrega em km: '))

           
            
            if dis <= 2 or total_mar >= 80:
                taxa = 0 
                print('Frete gratis')
            elif dis <= 5 :
                taxa = 5
            elif dis <= 8:
                taxa = 8
            else :  
                print('Pedido para retirada no local')
                taxa = 0



            total_fre = total_mar + taxa
             

            print('\n--- RESUMO DO PEDIDO ---')
            print('Valor das marmitas: R$', total_mar)
            print('Valor da entrega: R$', taxa)
            print('Total do pedido: R$', total_fre)

    elif opcao == 2:
        print('Fechamento do dia')

    elif opcao == 0:
        print('Programa encerrado')

    else:
        print('Opção não identificada')