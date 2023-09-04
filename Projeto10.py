n = int(input("Digite um número com três digitos: "))
print(f'Número informado: {n}')

# ni = int(str(n)[::-1])

d1 = n // 100
d2 = n % 100
d2 = d2 / 10

d3 = d2 // 10
d4 = d2 % 10
d4 = d4 / 1

print(d1, d2, d3, d4)

# print(f'Número invertido: {ni}')


