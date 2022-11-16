#a lista livros deve armazenar o nome do o código e o nome do livro, o isbn, a quantidade de paginas e o autor
acervo_livros = list() 

#cadastrar livro
def cadastrar_livro(codigo, nome, isbn, paginas, autor):
  livro_aux = list()
  livro_aux = [codigo, nome, isbn, paginas, autor]
  acervo_livros.append(livro_aux .copy())
  livro_aux.clear()

#agora vamos montar uma forma de impressão 
def imprimir_acervo():
  print('Imprimindo o acervo atualizado:')
  for livro in acervo_livros:
    print(f"Livro {livro[1]}\n Código {livro[0]}\n ISBN: {livro[2]}\n Páginas: {livro[3]}\n Autor: {livro[4]}\n")

#removendo o livro pelo nome
def remover_livro(aux_nome_livro):
  removeu = False
  for livro in acervo_livros:
    if livro[1] == aux_nome_livro:
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
    if livro[1] == aux_nome_livro:
      livro.pop(3)
      livro.insert(3, aux_qtd_paginas)
      
      atualizou = True
      break
  return True

#adicionando um novo livro sem ser de forma explicíta;
for i in range(1):
  codigo = int(input('Digite o código:'))
  nome = str(input('Digite o nome:'))
  isbn = int(input('Digite o isbn:'))
  paginas = int(input('Digite a quantidade de páginas:'))
  autor = str(input('Digite o nome do autor:'))  
  cadastrar_livro(codigo, nome, isbn, paginas, autor)

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