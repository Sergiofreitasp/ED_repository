import reuniaolist
import main

def ousuariomenu():
    print(reuniaolist.reunioespublicas)

    opcao = str(input("Escolha uma opção:\n"
                       "1(criar reuniao)\n"
                       "2(confirmar presença)\n"
                       "3(vizualizar ata de reuniao)\n"
                       "4(baixar ata de reuniao)\n"
                       "5(Adicionar participantes)\n"
                      "6( Editar atas de reuniões do qual é o proprietário)\n"
                      "7 (Negar presença)\n"
                      "8 (Sair)"))
    if opcao == "1":
         print("CRIAR REUNIAO")
         tipo = str(input("Coloque o tipo de reunião publica(1) privada(2)"))
         if tipo == "1":
             reuniaolist.criarreuniaoPrO()
         elif tipo == "2":
              reuniaolist.criarreuniaoPrO()
    elif opcao == "2":
        print("CONFIRMAR PRESENÇA")
        reuniaolist.confirmarpresença()
    elif opcao == "3":
        reuniaolist.visualizaratasOutro()
    elif opcao == "4":
        reuniaolist.salvaratareuniaoOutro()
    elif opcao == "5":
        print("ADICIONAR PARTICIPANTES")
        reuniaolist.outroaddparticipantes()
    elif opcao == "6":
         reuniaolist.editaratasOutro()
    else:
        main.menu1()


