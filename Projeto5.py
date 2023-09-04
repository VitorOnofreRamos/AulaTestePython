peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))

IMC = peso / altura ** 2

print(f'Índice de Massa Corpórea é: {round(IMC, 2)}')
