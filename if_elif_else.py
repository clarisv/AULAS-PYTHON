'''
o programa exibe qual fruta foi mais vendida.

macas = int(input('digite a quantidade de maças vendidas: '))

bananas = int(input('digite a quantidade de bananas vendidas: '))

if macas > bananas:
    print('as maças tiveram mais vendas!')
elif bananas > macas:
    print('as bananas tiveram mais vendas!')
else:
    print('a quantidade de bananas e maças vendida foram as mesmas')'''



'''
o programa informa o tempo total de dias para estudar

A = int(input('informe os dias para a atividade A: '))
B = int(input('informe os dias para a atividade B: '))
C = int(input('informe os dias para a atividade C: '))

if A < 0 or  B < 0 or C < 0:
  print('erro: os dias nao podem ser negativos')
else:
    total_dias = A + B + C
    print(f'o tempo total de dias é: {total_dias}')'''



'''
o programa analisa se a temperatura é aceitavel

temperatura_atual = int(input('digite a temperatura atual: '))

if temperatura_atual > 25:
    print('alerta! temperatura a cima do limite permitido')
else:
    print('temperatura em niveis aceitaveis')'''


'''
calcula o imc

peso = float(input('digite seu peso em (kg): '))
altura = float(input('digite sua altura em (m):'))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com peso normal.")
else:
    print("Você está acima do peso.")'''


'''

calcula se os gastos estão dentro do orçamento

orcamento = float(input('digite o seu gasto do mes (R$): '))

if orcamento > 3000:
    print('atençao! voce passou do seu orçamento.')
else:
    print('seus gastos estão dentro do seu orçamento')'''
