# Exercicio 1
Colocacao = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Barcelona"]
print(Colocacao[0:3])
print(Colocacao[-2:])
print(sorted(Colocacao))
print(Colocacao.index("Barcelona"))

# Exercicio 2
Loja_1 = {"S20", "S21", "S24"}
Loja_2 = {"iPhoneX", "iPhone11", "iPhone14", "iPhone15"}
print("A loja 1 vende ", len(Loja_1), " celulares, sendo eles: ", Loja_1)
print("A loja 2 vende ", len(Loja_2), " celulares, sendo eles: ", Loja_2)

# Exercicio 3
Nome = input("Qual o nome do aluno? ")
Media = int(input("Qual a media do aluno? "))
while not (0 <= Media <= 100): # Python e ridiculo
    Media = int(input("Media invalida. Insira um valor entre 100 e 0: "))
Sistema = {"Nome": Nome, "Media": Media, "Final": "NC"}
if Sistema["Media"] >= 50:
    Sistema["Final"] = "Aprovado"
else:
    Sistema["Final"] = "Reprovado"
print(Sistema)

# Exercicio 4
Ficha = {}

for i in range(0,3):
    Nome = input("Qual o nome da pessoa? ")
    Peso = float(input("Qual o peso da pessoa? "))
    Ficha[Nome] = Peso
Mais_pesado = max(Ficha, key=Ficha.get)
print("O mais pesado e", Mais_pesado)
Mais_leve = min(Ficha, key=Ficha.get)
print("O mais leve e", Mais_leve)

# Exercicio 5
n = int(input("Quantas pessoas deseja cadastrar? "))

soma_idades = 0
mulheres_menos_20 = 0

for i in range(n):
    print(f"\nPessoa {i + 1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    soma_idades += idade

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idades / n

print(f"\nMédia de idade do grupo: {media_idade:.2f}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
