"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de
alunos com média maior ou igual a 7.0.
"""
lista_alunos = list()

def validar_nota(aux_numero):
  valido = True
  try:
    aux_numero = float(aux_numero)
  except:
    valido = False
    print('Nota inválida digite novamente')
  return valido
  
def salvar_notas(qtd_notas):
  lista_notas = list()
  lista_notas.clear()
  for i in range(qtd_notas):
    aux_nota = input('Informe a nota:')
    while True:
      if validar_nota(aux_nota):
        lista_notas.append(float(aux_nota))
        break
      else:
        aux_nota = input('Informe a nota:')
  return lista_notas

def cadastrar_aluno():
  nome = str(input('Informe o nome do aluno:'))
  #qtd_notas = int(input('Informe quantas notas deseja salvar'))
  qtd_notas = 4
  notas = salvar_notas(qtd_notas)
  media = sum(notas) / len(notas)
  aluno = dict()
  aluno["Nome"] = nome
  aluno["Notas"] = notas
  aluno["Média"]  = media

  lista_alunos.append(aluno.copy())
  aluno.clear()

def quantidade_alunos_media_sete():
  qtd_alunos = 0
  for aluno in lista_alunos:
    if aluno['Média'] >= 7.0:
        qtd_alunos += 1
  print(f"Existem {qtd_alunos} alunos com média maior ou igual a 7.0")
  
def imprimir_lista_alunos():
  for aluno in lista_alunos:
    print(aluno)

for i in range(3):
  cadastrar_aluno()

imprimir_lista_alunos()  

quantidade_alunos_media_sete()