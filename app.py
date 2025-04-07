import os

def exibir_nome_doprograma():
 print('sabor express\n')

def exibir_opcoes():
    print(' 1 - cadastrar restaurante')
    print(' 2 - listar restaurante')
    print(' 3 - ativar restaurante')
    print(' 4 - sair\n')

def finalizar_app():
    os.system('cls')
    print('finalizando app\n')

def escolher_opcao():
    opcao_escolhida = int (input('escolha uma opcao:'))
    # opcao_escolhida = int(opcao_escolhida)



    if opcao_escolhida == 1:
        print('cadastrar restaurante ')
    elif opcao_escolhida == 2:
        print('listar restaurante')
    elif opcao_escolhida == 3:
        print('ativar restaurante')
    else: 
        finalizar_app()

def main():
    exibir_nome_doprograma()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()