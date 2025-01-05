# Importando a biblioteca random
import random
# Entrada dos alunos
qnt_aluno = int(input('Quantos alunos participarão? '))
nomes_aluno = []
for i in range(qnt_aluno):
  nome = str(input(f'Digite o nome do aluno {i+1}: '))
  nomes_aluno.append(nome)
# Exceção
if 'Samuel' in nomes_aluno:
   print(f'A pessoa escolhida para limpar o quadro foi... Samuel!')
else:
# Dicionario relacionando alunos à números
# e contador
 dicionario = {}
 contador = 1
# Adicionando alunos ao dicionario
 for nomes in nomes_aluno:
    dicionario[contador] = nomes
    contador += 1
# Aleatorizando o aluno
 valor = random.randint(1, qnt_aluno)
# Saida
 print(f'A pessoa escolhida para limpar o quadro foi... {dicionario[valor]}!')