#a lista livros deve armazenar o nome do o código e o nome do livro, o isbn, a quantidade de paginas e o autor
acervo_livros = list() 

def validar_inteiro(aux_numero):
  valido = True
  try:
    aux_numero = int(aux_numero)
  except:
    valido = False
    print('O número digitado é inválido, tente novamente.')
  return valido

def validar_float(aux_numero):
  valido = True
  try:
    aux_numero = float(aux_numero)
  except:
    valido = False
    print('O número digitado é inválido, tente novamente, digitando um número com casas decimais usando .')
  return valido

def validar_string(aux_texto):
  valido = True
  try:
    aux_texto =  float(aux_texto)
    valido = False
  except:
    print('O texto informado é um número, digite novamente.')
  return valido
  
#cadastrar livro
def cadastrar_livro(codigo, nome, isbn, paginas, autor, valor):
  aux_livro = dict()
  aux_livro['Codigo'] = codigo
  aux_livro['Nome'] = nome
  aux_livro['Isbn'] = isbn
  aux_livro['Paginas'] = paginas
  aux_livro['Autor'] = autor
  aux_livro['Valor'] = valor
  acervo_livros.append( aux_livro.copy())
  aux_livro.clear()

#agora vamos montar uma forma de impressão 
def imprimir_acervo():
  print('Imprimindo o acervo atualizado:')
  for livro in acervo_livros:
    print("Informações do Livro:")
    for chave, valor in livro.items():
      print(f"{chave}: {valor}")
  print("\n")

#removendo o livro pelo nome
def remover_livro(aux_nome_livro):
  removeu = False
  for livro in acervo_livros:
    if livro['Nome'] == aux_nome_livro:
      acervo_livros.remove(livro)
      removeu = True
      break
  return removeu

#removendo o ultimo livro do acervo
def remover_ultimo():
  acervo_livros.pop()

#atualizando um determinado livro e suas paginas
def atualizar_livro(aux_qtd_paginas, aux_nome_livro):
  atualizou = False
  for livro in acervo_livros:
    if livro['Nome'] == aux_nome_livro:
      livro['Paginas'] = aux_qtd_paginas
      atualizou = True
      break
  return atualizou

#criando dicionarios teste
cadastrar_livro(1, 'Java', '123', 102, "Fulano 1", 150.00)
cadastrar_livro(2, 'Python', '1234', 104, "Fulano 2", 165.98)
cadastrar_livro(3, 'C#', '1547', 99, "Fulano 3", 198.00)
cadastrar_livro(4, 'C++', '963', 88, "Fulano 4",178.90)

#adicionando um novo livro sem ser de forma explicíta;
for i in range(1):
  codigo = str(input('Digite o código:'))
  while True:
    if validar_inteiro(codigo):
      nome = str(input('Digite o nome:'))
      isbn = str(input('Digite o isbn:'))
      paginas = str(input('Digite a quantidade de páginas:'))
      autor = str(input('Digite o nome do autor:'))  
      valor = float(input('Digite o valor do livro:'))  
      cadastrar_livro(codigo, nome, isbn, paginas, autor, valor)
      break
    else:
      codigo = str(input('Digite o código:'))
      if validar_inteiro(codigo):
        nome = str(input('Digite o nome:'))
        isbn = str(input('Digite o isbn:'))
        paginas = str(input('Digite a quantidade de páginas:'))
        autor = str(input('Digite o nome do autor:'))  
        valor = float(input('Digite o valor do livro:'))  
        cadastrar_livro(codigo, nome, isbn, paginas, autor, valor)
        break
      else:
        continue
        


imprimir_acervo()

nome_livro = str(input('Informe o nome do livro que deseja remover:'))
remover_livro(nome_livro)
imprimir_acervo()

remover_ultimo()
imprimir_acervo()

nome_livro2 = str(input('Informe o nome do livro que deseja atualizar:'))
qtd_paginas = int(input('Informe a nova quantidade de páginas do livro'))
atualizar_livro(qtd_paginas, nome_livro2)
imprimir_acervo()