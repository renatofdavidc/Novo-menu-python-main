import time

def exibirMenu():
    print('====================== MEU CARRO PORTO ======================')
    print('Seja bem vindo ao app Meu Carro Porto!')
    print('====================== MENU PRINCIPAL ======================')
    print('[1] - Onde posso acessar o site da Porto?')
    print('[2] - Agendar manutenção')
    print('[3] - Chamar um mecânico')
    print('[4] - Calculadora de economia do Meu Carro Porto')
    print('[5] - O que é o app Meu Carro Porto?')
    print('[6] - Sair do aplicativo')

def tela1():
    print('====================== ACESSO SITE DA PORTO ======================')
    print('Você pode acessar o site da porto pelo link: https://www.portoseguro.com.br/seguro-auto')
    print('Retornando ao menu principal em 10 segundos...')
    time.sleep(10)
    exibirMenu()

mes = []
dia = []
def tela2():
    print('====================== AGENDAR MANUTENÇÃO ======================')
    print('[1] - Exibir minhas manutenções agendadas')
    print('[2] - Agendar uma manutenção')
    print('[3] - Cancelar uma manutenção')
    print('[4] - Retornar ao menu principal')
    escolha = input('Escolha uma opção: ')

    match escolha:
        case '1':
            print('As manutenções agendadas são, respectivamente em cada lista:')
            print('Dia: ', dia)
            print ('Mês: ', mes)
            print('Você retornará ao menu anterior em 10 segundos...')
            time.sleep(10)
            tela2()
        case '2':
            escolhames = input('Escolha um mês (1-12): ')
            escolhadia = input('Escolha um dia do mês (ex: 1, 16, 30...): ')
            mes.append(escolhames)
            dia.append(escolhadia)
            print(f'Consulta agendada para o dia {escolhadia}/{escolhames}!')
            time.sleep(5)
            tela2()
        case '3':
            print('As manutenções agendadas são, respectivamente em cada lista:')
            print('Dia: ', dia)
            print ('Mês: ', mes)
            deletar = int(input('Digite o número da manutenção que deseja deletar: '))
            i = deletar - 1
            del(dia[i])
            del(mes[i])
            print('Manutenção cancelada!')
            time.sleep(5)
            tela2()
        case '4':
            exibirMenu()
        case _:
            print('Opção inválida! Você será encaminhado ao menu principal em 5 segundos...')
            time.sleep (5)
            exibirMenu()

rua = []
numerocasa = []
bairro = []
i = 0

def tela3():
    print('====================== CHAMAR UM MECÂNICO ======================')
    print('[1] - Registrar um endereço para envio de mecânico (máximo de 5)')
    print('[2] - Escolher um endereço para ser enviado um mecânico')
    print('[3] - Visualizar endereços registrados')
    print('[4] - Remover um endereço')
    print('[5] - Retornar ao menu principal')
    escolhaOpcao = input('Digite uma opção: ')
    def definirEndereco():
        bairroinput = input('Por favor, digite seu bairro: ')
        bairro.append(bairroinput)
        ruainput = input('Por favor, digite sua rua: ')
        rua.append(ruainput)
        numerocasainput = input('Por favor, digite o número da sua casa:')
        numerocasa.append(numerocasainput)
        tela3()
    def escolherUmEndereco():
        i = int(input('Para qual endereço deve ser enviado o guincho? Escolha um número de 1 a 5: '))-1
        if (i < 0 or i >=len(rua)):
            print('Opção inválida! Em 5 segundos você será encaminhado ao menu anterior...')
            time.sleep(5)
            tela3()
        else:
            print(f'Um guincho será enviado para o seguinte endereço: Bairro: {bairro[i]}, Rua: {rua[i]}, Número: {numerocasa[i]}')
            time.sleep(5)
            exibirMenu()
    def visualizarEnderecos():
        print('Os endereços registrados são, respectivamente em cada lista:')
        print(f'Rua: {rua}')
        print(f'Bairro: {bairro}')
        print(f'Número da casa: {numerocasa}')
        print('Retornando ao menu anterior em 10 segundos...')
        time.sleep(10)
        tela3()
    def removerEndereco():
        print(f'Os endereços registrados são: ')
        print(f'Rua: {rua}')
        print(f'Bairro: {bairro}')
        print(f'Número da casa: {numerocasa}')
        print('Se não desejar excluir um endereço, digite 6.')
        enderecodeletado = input('Qual endereço você deseja excluir?(Escolha um número de 1 a 5) ')
        match enderecodeletado:
            case '6':
                tela3()
            case '1':
                del(rua[0])
                del(numerocasa[0])
                del(bairro[0])
                print('Itens removidos.')
                time.sleep(3)
                tela3()
            case '2':
                del(rua[1])
                del(numerocasa[1])
                del(bairro[1])
                print('Itens removidos.')
                time.sleep(3)
                tela3()
            case '3':
                del(rua[2])
                del(numerocasa[2])
                del(bairro[2])
                print('Itens removidos.')
                time.sleep(3)
                tela3()
            case '4':
                del(rua[3])
                del(numerocasa[3])
                del(bairro[3])
                print('Itens removidos.')
                time.sleep(3)
                tela3()
            case '5':
                del(rua[4])
                del(numerocasa[4])
                del(bairro[4])
                print('Itens removidos.')
                time.sleep(3)
                tela3()
            case _:
                print('Opção inválida, você será encaminhado ao menu anterior em 5 segundos...')
                time.sleep(5)
                tela3()

    match escolhaOpcao:
        case '1':
            definirEndereco()
        case '2':
            if len(rua) == 0:
                print('Por favor, registre um endereço primeiro!')
                definirEndereco()
            else:
                escolherUmEndereco()
        case '3':
            if len(rua) == 0:
                print('Por favor, registre um endereço primeiro!')
                definirEndereco()
            else:
                visualizarEnderecos()
        case '4':
            removerEndereco()
        case '5':
            exibirMenu()
        case _:
            print('Opção inválida! Em 5 segundos você será enviado para o menu principal...')
            time.sleep(5)
            exibirMenu()

def tela4():
    def calculoKmL():
        km = float(input('Por favor, informe quantos quilômetros foram rodados com o carro: '))
        litros = float(input('Agora, por favor informe quantos litros de combustível foram consumidos:'))
        media = km/litros
        print(f'O carro está fazendo {media} Km/L')
        if media <= 5:
            print('O carro não é econômico')
        elif media > 5 and media <= 8.5:
            print('O carro tem um consumo ok')
        elif media > 8.5:
            print('O carro é econômico')
    def verMedia():
        kml = float(input('Por favor, informe quantos Km/L o carro está fazendo: '))
        if kml <= 5:
            print('O carro não é econômico')
        elif kml > 5 and kml <= 8.5:
            print('O carro tem um consumo ok')
        elif kml > 8.5:
            print('O carro é econômico')
    print('====================== CALCULADORA DE ECONOMIA ======================')
    print('[1] - Desejo saber quantos km/L meu carro faz')
    print('[2] - Já sei quantos km/L meu carro faz, desejo apenas saber quão econômico ele é')
    print('[3] - Retornar ao menu principal')
    opcao = input('Digite uma opção: ')
    match opcao:
        case '1':
            calculoKmL()
        case '2':
            verMedia()
        case '3':
            exibirMenu()

def tela5():
    print('====================== O QUE É O APP MEU CARRO PORTO? ======================')
    print('O aplicativo Meu Carro Porto é um sistema desenvolvido em Python para proporcionar ao cliente dos seguros porto \n uma melhor experiência ao realizar manutenções e consertos em seus carros, com interface simples e intuitiva.')
    print('====================== INTEGRANTES ======================')
    print('Celso Canaveze Teixeira Pinto')
    print('Henrique Nascimento')
    print('Renato de Freitas David Campiteli')
    time.sleep(10)
    
def main():
    while True:
        exibirMenu()
        escolhaPrincipal = input('Escolha uma opção: ')

        match escolhaPrincipal:
            case '1':
                tela1()
            case '2': 
                tela2()
            case '3':
                tela3()
            case '4':
                tela4()
            case '5':
                tela5()
            case '6':
                break
            case _:
                print('Opção inválida! Por favor, digite novamente.')
if __name__ == "__main__":
    main()
