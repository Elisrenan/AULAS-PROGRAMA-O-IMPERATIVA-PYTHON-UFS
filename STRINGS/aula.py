materia = 'PROGRAMAÇÃO'
         
print('A matéria é ', materia)

#acessando uma posição de uma determinada string
letra = materia[2]

print('A letra escolhida foi ',letra)


#acessar parte de uma palavra ou texto
parte_palavra = materia[1:5]
print('Parte da palavra ',parte_palavra)


#acessar do texto ou palavra a partir de um indice
parte_palavra_sufixo = materia[2:]
print('Parte da palavra sufixo ',parte_palavra_sufixo)

#acessar do texto ou palavra a partir de um indice
parte_palavra_prefixo = materia[:5] 
print('Parte da palavra prefixo ',parte_palavra_prefixo)

materia = 'PROGRAMAÇÃO'
materia_2 = 'programação'

if materia == materia_2:
  print('são iguais')
else:
  print('São diferentes')

# USO DO IN
if 'm' in materia:
  print('Existe essa letra - uso do in')
else:
  print('Não existe essa letra - uso do in')


if 'M' in materia:
  print('Existe essa letra - uso do in')
else:
  print('Não existe essa letra - uso do in')


#USO DO NOT IN
if 'm' not in materia:
  print('Não existe essa letra - uso do not in')
else:
  print('Existe essa letra - uso do not in')

#concatenando strings
texto = 'A matéria escolhida foi '+materia+', parabéns!'
print(texto)

#usando multiplicação dentro de uma string
multip_string = 'texto inicio '+('\n' * 3)+' texto fim'
print(multip_string)

#deixando a primeira de uma palavra em maiuscula - usando como
#exemplo a variavel materia_2
prim_letra_maius = materia_2.capitalize()
print('Variavel com a primeira letra em minusculo ',materia_2)
print('Variavel com a primeira letra em maiusculo ',prim_letra_maius)

#usando a função count para contar palavras ou letras dentro de um texto
letra = 'o'
qtd_letra = materia_2.count(letra)
print('Existem {} letras do tipo {}'.format(qtd_letra,letra))

#utilizando o split
texto_2 = 'Copa do mundo de 2014'
        #    0  1    2    3   4
lista_palavras = texto_2.split()
print(lista_palavras)
print('\n '*3)

print('Acessando uma palavra o ',lista_palavras[3])
print('\n '*3)

print('Acessando uma palavra e depois uma de suas letras que é o: ',lista_palavras[3][0])
print('\n '*3)

#utilizando a função len()
qtd_v1 = len(texto_2)
qtd_v2 = len(lista_palavras)
print('Existem {} caracteres na variavel texto2'.format(qtd_v1))

print('Existem {} caracteres na variavel lista_palavras'.format(qtd_v2))

print('\n '*3)

#verificando se existe uma parte da palavra no inicio ou no fim de um texto
texto_3 = 'A vida é bela para quem tem coragem'

if texto_3.startswith('A vida'):
  print('Existe A vida no inicio do texto')

if texto_3.endswith('coragem'):
  print('Existe coragem no fim do texto')


print('\n '*3)


#conteudo está na pasta funções