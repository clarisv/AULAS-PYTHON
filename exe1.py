
def verificador_de_idade():
    print('Verificando se o usuario é Criança, Adolescente ou Adulto')
    idade = int(input('Digite sua idade: '))
    if idade <= 12:
        print(f'{idade} o usuario é uma crianca')
    elif idade > 12 and idade <= 17:
        print(f'{idade} o usuario é um adolescente')
    else:
        print(f'{idade} o usuario é um adulto') 

verificador_de_idade()