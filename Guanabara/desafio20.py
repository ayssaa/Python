# Esse programa lê X nomes de alunos e,
# aleatoriamente, escolhe a ordem de apresentação
# dos alunos
import random
qnt_alunos = int(input('Quantos alunos participarão? '))
nome_alunos = []

# Dado uma quantidade de alunos, receber seus nomes
for aluno in range(qnt_alunos):
    nome_aluno = str(input(f'Digite o nome do aluno {aluno+1}: '))
    nome_alunos.append(nome_aluno)

# Criando um dicionario
dicionario = {}
contador = 1

# Criando o conteudo do dicionario
for nome in nome_alunos:
    dicionario[contador] = nome
    contador += 1

# Aleatorizando e criando lista da ordem
lista_ordem = []
while len(lista_ordem) != qnt_alunos:
  valor = random.randint(1, qnt_alunos)
  if valor not in lista_ordem:
        lista_ordem.append(valor)

# Lendo lista e mostrando os alunos
contador2 = 1
for colocacao in lista_ordem:
    print(f'A ordem escolhida para a apresentação foi... Em {contador2}° {dicionario[colocacao]}!')
    contador2 += 1  