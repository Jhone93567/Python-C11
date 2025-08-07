# Exercicio 1
nome = input('Qual o seu nome? ')
print('Nome maiusculo:', nome.upper())
print('Nome minusculo:', nome.lower())
print('Quantidade de letras no nome:', len(nome))
print('Se seu ultimo nome fosse \"do Inatel\", seria assim:', nome.replace(nome.split()[-1], 'do Inatel'))

# Exercicio 2
tabuada = int(input('Entre com um número para ver sua tabuada: '))
intervalo = int(input('Quantos números da tabuada você quer ver? '))
print('Tabuada do', tabuada)
for i in range(1, intervalo + 1):
    print(tabuada, 'x', i, '=', tabuada * i)

# Exercicio 3
sexo = input('Qual o seu sexo? (M/F) ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Qual o seu sexo? (M/F) ').upper()
if sexo == 'M':
    print('Você é do sexo masculino.')
else:
    print('Você é do sexo feminino.')

# Exercicio 4
distancia = float(input('Entre com a distância em km: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da passagem é:', preco)

# Exercicio 5
numero = int(input('Entre com um número entre 1000 e 9999: '))
while numero < 1000 or numero > 9999:
    numero = int(input('Número inválido. Entre com um número entre 1000 e 9999: '))
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000
print('Unidade:', unidade)
print('Dezena:', dezena)
print('Centena:', centena)
print('Milhar:', milhar)

# Exercicio 6
import math
numero = float(input('Entre com um número decimal: '))
print('Raiz quadrada:', math.sqrt(numero))
print('Funcao teto:', math.ceil(numero))
print('Funcao piso:', math.floor(numero))
print('Sua parte inteira:', math.trunc(numero))