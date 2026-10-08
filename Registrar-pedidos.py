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

      
   elif opcao == '2':
      print("Encerrando Atendimento")
      break
   else:
      print("Mensagem invalida!")
      


