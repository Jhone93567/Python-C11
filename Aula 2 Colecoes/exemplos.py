# Exemplos com tuplas
tupla = ('Goku', 'Vegeta', 'Trunks', 'Gohan') # Para declarar tuplas usamos (), tupla e uma colecao imutavel e nao permite alteracoes
print(tupla) # Mostrando elementos

#tupla[0] = 'Bulma' <- Isso resulta em erro

print(tupla[1:3]) # Podemos acessar os elementos como vetor, lembrar que o primeiro argumento e inclusivo e o ultimo e exclusivo

print(tupla[:2]) # Nao passar o primeiro argumento faz com que percorra do comeco ate o segundo argumento, lembre se que em python o segundo argumento e excludente

print(tupla[2:]) # Nao passar o segundo argumento faz com que percorra a partir do primeiro argumento ate o final

print(tupla[-2]) # Podemos passsar indices negativos

# Funcoes pre prontas
print(len(tupla)) # Tamanho da tupla
print(max(tupla)) # Maximo da tupla, ordem alfabetica para strings, nao e possivel usar entre tipos
print(min(tupla)) # Minimo da tupla, ordem alfabetica ^^


# Exemplos com listas
lista = ['Goku', 'Vegeta', 'Trunks', 'Gohan'] # Para declarar listas usamos [], listas sao colecoes mutaveis
print(lista) # Mostrando elementos

lista.append('Bulma') # Inserindo elementos no fim

lista.insert(1, 'Kuririn') # Inserindo elementos onde quisermos
print(lista)

lista[0] = 'Piccolo' # Alterando elementos
print(lista)

del lista[0] # Deleta o elemento na posicao 0, pelo indice
lista.remove('Bulma') # Deletando pelo valor
print(lista)

if 'Vegeta' in lista: # Verifica se o elemento existe na lista
    lista.remove('Vegeta')
print(lista)

sorted(lista) # Funcao do python que retorna a colecao ordenada
print(lista)

lista.sort(reverse=True) # Funcao das listas para ordenar, o argumento reverse ordena em forma decrescente
print(lista)

lista.sort()
print(lista)


# Exemplos com conjuntos
conjunto = {'Goku', 'Vegeta', 'Trunks', 'Gohan', 'Goku'} # Para declarar conjuntos usamos {}, os conjuntos sao colecoes nao ordenadas e que nao admitem elementos duplicados
print(conjunto) # Imprime o conjunto, note que goku so aparece 1 vez e a ordem nao e diferente pra cada print

conjunto.add('Piccolo') # Adiciona um elemento
conjunto.add('Goku') # Nao faz nada ja que ja existe um goku

conjunto.remove('Goku') # Remove pelo nome


# Descobrindo o tipo de algo em Python
print(type(conjunto))


# Exemplos com dicionario
dicionario = {'Key': 'Value', 'Chave': 'Valor'} # Para declarar dicionarios, usamos {} tambem, porem usamos Key-Value atribuindo um valor para cada chave
print(dicionario)

dicionario['Nome'] = 'Renzo' # Add

dicionario['Key'] =  42 # Update

del dicionario['Key'] # Delete
print(dicionario)

dicionario['familia'] = ['Gohan', 'Goten', 'Chichi', 'Pan'] # Conseguimos colocar uma colecao dentro de outra
print(dicionario)

print(dicionario['familia'][-2]) # Acessando a lista dentro do dicionario