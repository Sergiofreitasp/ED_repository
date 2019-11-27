import reuniaolist
import main
def omenuC():
    opcao = str(input("Escolha uma opção - 1(criar reuniao) 2(confirmar presença) 3(vizualizar ata de reuniao)"
                      "/n 4(editar ata de reuniao) 5(baixar ata de reuniao) 6(adicionar participantes as reuniões)/n "
                      "/n 7(negar presença)"))
    if opcao == "1":
        print("CRIAR REUNIAO")
        tipo = str(input("Coloque o tipo de reunião publica(1) privada(2)"))
        if tipo == "1":
            return reuniaolist.criarreuniaoPuC()
        elif tipo == "2":
            return reuniaolist.criarreuniaoPrC()
    elif opcao == "2":
        print("CONFIRMAR PRESENÇA")
    elif opcao == "3":
        return reuniaolist.visualizaratasCordenador()
    elif opcao == "4":
        return reuniaolist.editaratasCordenador()
    elif opcao == "5":
        return reuniaolist.salvaratareuniaoCordenador()
    elif opcao == "6":
        print("ADICIONAR PARTICIPANTE")
    elif opcao == "7":
        print("Negar presença")
    else:
        return main.menu1()
