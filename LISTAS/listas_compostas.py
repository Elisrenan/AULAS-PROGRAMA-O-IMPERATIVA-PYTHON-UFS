#a lista livros deve armazenar o nome do o código e o nome do livro, o isbn, a quantidade de paginas e o autor
acervo_livros = list() 
#para facilitar o teste vou criar quatro listas explicitas
livro_aux = list()

livro_aux  = [1, 'Java', 147258, 120, 'João Bosco']
acervo_livros.append(livro_aux .copy())
livro_aux .clear()

livro_aux  = [2, 'Python', 369258, 98, 'Elisrenan Barbosa']
acervo_livros.append(livro_aux .copy())
livro_aux .clear()

livro_aux  = [3, 'PHP', 258789, 80, 'Francisco']
acervo_livros.append(livro_aux .copy())
livro_aux .clear()

livro_aux = [4, 'Node JS', 654789, 158, 'Murilo Mendez']
acervo_livros.append(livro_aux .copy())
livro_aux.clear()

#agora vamos montar uma forma de impressão 
for livro in acervo_livros:
  print(f"Livro {livro[1]}\n Código {livro[0]}\n ISBN: {livro[2]}\n Páginas: {livro[3]}\n Autor: {livro[4]}\n")

#adicionando um novo livro sem ser de forma explicíta;
for i in range(1):
  codigo = int(input('Digite o código:'))
  nome = str(input('Digite o nome:'))
  isbn = int(input('Digite o isbn:'))
  paginas = int(input('Digite a quantidade de páginas:'))
  autor = str(input('Digite o nome do autor:'))
  #apos inserir todos os dados digitado pelo o usuário na lista auxiliar, vamos realizar uma copita dos dados e inserir a lista auxiliar na lista do acervo e vamos inserir na segunda posição
  livro_aux = [codigo, nome, isbn, paginas, autor]
  acervo_livros.append(livro_aux .copy())
  livro_aux.clear()

print('Imprimindo o acervo atualizado:')
for livro in acervo_livros:
  print(f"Livro {livro[1]}\n Código {livro[0]}\n ISBN: {livro[2]}\n Páginas: {livro[3]}\n Autor: {livro[4]}\n")

#remover o livro de Java
for livro in acervo_livros:
  if livro[1] == 'Java':
    acervo_livros.remove(livro)
    break

print('Imprimindo o acervo atualizado:')
for livro in acervo_livros:
  print(f"Livro {livro[1]}\n Código {livro[0]}\n ISBN: {livro[2]}\n Páginas: {livro[3]}\n Autor: {livro[4]}\n")

#removendo o ultimo livro do acervo
acervo_livros.pop()

print('Imprimindo o acervo atualizado:')
for livro in acervo_livros:
  print(f"Livro {livro[1]}\n Código {livro[0]}\n ISBN: {livro[2]}\n Páginas: {livro[3]}\n Autor: {livro[4]}\n")


#atualizando o livro de Python
for livro in acervo_livros:
  if livro[1] == 'Python':
    livro.pop(3)
    livro.insert(3, 500)
    break

print('Imprimindo o acervo atualizado:')
for livro in acervo_livros:
  print(f"Livro {livro[1]}\n Código {livro[0]}\n ISBN: {livro[2]}\n Páginas: {livro[3]}\n Autor: {livro[4]}\n")