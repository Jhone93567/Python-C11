print('Olá Python') #somente texto
print(7+7) #operações matemáticas
print('O resultado de 7 + 7 é', 7+7) #texto + operações

nome = 'Vincent' #str
idade = 30 #int
peso = 83.5 #float
print(nome, idade, peso)

nome = input('Qual o seu nome?')
idade = int(input('Qual sua idade?'))
peso = float(input('Qual o seu peso?'))
print('Seu nome é {} sua idade {} e seu peso {}.'.format(nome,idade,peso))

var = 'Hello World'

var[6] #captura a letra W da String
var[:5] #captura a palavra Hello
var[6:11] #captura a palavra World (6 inclusive e 11 exclusive)
var[6:] #também captura a palavra World
var[0:10:2] #mostra HloWrd (ou seja, pula de 2 em 2)

len(var) #retorna o número de caracteres de uma String
var.count('o') #conta o número de o’s da palavra
var.count('l',0,5) #conta quantos l’s tem dentro de Hello
var.find('lo') #indica a posição de onde começa 'lo'
'World' in var #retorna True se a palavra se encontrar dentro do texto
var.replace('World', 'Python') #troca uma palavra por outra no texto
var.upper() #todas as letras do texto ficam MAIÚSCULAS
var.lower() #todas as letras do texto ficam MINÚSCULAS
var.split() #quebra o texto em partes

idade = int(input('Entre com sua idade:'))
if idade < 18:
    print('Você é menor de idade')
else:
    print('Você é maior de idade')

for c in range(0,10): #mostrando um conteúdo x vezes
    print('Python é legal')
for c in range(0,10): #a variável c assume um novo valor a cada iteração
    print(c)
for c in range (10,0,-1): #realizando uma contagem regressiva
    print(c)

var = 1 
while var < 5:
    print(var)
    var +=1
senha = ''
while senha != 'python123':
    senha = input('Entre com a senha correta:')
print('Bem-vindo ao sistema! ☺')