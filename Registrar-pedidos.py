# Gabriel Vilela Cardoso de Lima


marmitaP = 15.00

marmitaM = 18.00

marmitaG =  22.00





while  True:
   print("Opção 1 - Registrar Pedido")
   print("Opção 2 - Fechar o dia")
   opcao = input("Escolha uma das Opções? ")

   if opcao == '1' :
      qtd = int(input("Quantidade de Marmitas? "))
      while qtd <=0 or qtd >=11 :
           print("Quantidade invalida")
           qtd= int(input("Quantidades de Marmitas? "))
      total_marmitas = 0

      for s  in range(qtd):
           tamanho = input(f"Tamanho da Marmita {s+1}: P,M,G: ").upper()
           while tamanho not in['P','M','G']:
            print("Opção inválida!")
            tamanho = input(f"Tamanho da Marmita {s+1}: P,M,G: ").upper()

           if  tamanho == 'P':
               total_marmitas += marmitaP
           elif tamanho == 'M':
               total_marmitas +=marmitaM
           elif tamanho == 'G':
                total_marmitas +=marmitaG
      print(total_marmitas)
              


      
   elif opcao == '2':
      print("Encerrando Atendimento")
      break
   else:
      print("Mensagem invalida!")




      


