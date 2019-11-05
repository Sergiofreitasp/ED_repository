
reunioespublicas = []
reunioesprivadas = []



def ousuariomenu():

    opcao = str(input("Escolha uma opção - 1(criar reuniao) 2(confirmar ou negar presença) 3(vizualizar ata de reuniao)"
                      "/n 4(editar ata de reuniao) 5(baixar ata de reuniao) "))

    if opcao == "1":
        print("CRIAR REUNIAO")
    elif opcao == "2":
        print("CONFIRMAR PRESENÇA")
    elif opcao == "3":
        print("VIZUALIZAR ATA")
    elif opcao == "4":
        print("EDITAR ATA")
    elif opcao == "5":
        print("BAIXAR ATA")


ousuariomenu()


def criarreuniao():
    visibilidade = str(input("Sua reuniao é 1(publica) ou 2(privada)? "))

    assunto = str(input("Defina o assunto da sua reuniao: "))
    data = str(input("Defina a data da sua reuniao: "))
    local = str(input("Defina o local da sua reuniao: "))
    hinicial = str(input("Defina o horario de inicio da sua reuniao: "))
    hfinal = str(input("Defina o horario em que sua reuniao encerra: "))
    ata = str(input("Defina o horario em que sua reuniao encerra: "))






    criarreuniao()