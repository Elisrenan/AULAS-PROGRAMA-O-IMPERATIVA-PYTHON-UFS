print('\nForma um de criar um dicionário\n')
info_pessoa = dict()

info_pessoa['nome'] = 'Elisrenan'
info_pessoa['idade'] = 26

print(info_pessoa)

print('\nForma dois de criar um dicionario\n')

anime = {'nome': 'Naruto', 'temporada': 'Shippuden', 'ano': 2007}

print(anime)

print('\nFunções de um dicionário\n')
#os values trazem somente os valores contidos em um dicionário especifico
print(anime.values())
#os values trazem somente as chaves contidas em um dicionário especifico
print(anime.keys())
#os values trazem as chaves e os valores contidos em cada uma dessas chaves de um dicionário
print(anime.items())

print('\nUnindo listas com dicionarios\n')

netflix = list()

netflix.append(anime.copy())
anime.clear()
anime = {'nome': 'Boku no Hero', 'temporada': '4ª temporada', 'ano': 2021}

netflix.append(anime.copy())
anime.clear()
anime = {'nome': 'Boruto', 'temporada': 'Next Generation', 'ano': 2018}

netflix.append(anime.copy())
anime.clear()
print('A lista com os dicionários é:')
print(netflix)

print('\n Organizando a impressão da lista de dicionários \n')

print('forma um de imprimir varios dicionários')
for anime in netflix:
    print(anime)

print('\nforma dois de imprimir varios dicionários\n')
for aux_anime in netflix:
  for chave, valor in aux_anime.items():
    print(f'{chave} é {valor}')
  print('\n')

print('\n adicionando elemetos na lista de forma dinamica')
print('utilizando dicionários\n')

for i in range(0, 1):
  aux_anime = dict()
  aux_anime ['nome'] = str(input('Informe um nome:\n'))
  aux_anime ['temporada'] = str(input('Informe a temporada:\n'))
  aux_anime ['ano'] = int(input('Informe o ano:\n'))
  netflix.append(aux_anime.copy())
  aux_anime .clear()
  
print('\n Forma três de imprimir a lista com dicionarios')
for aux_anime in netflix:
  for valor in aux_anime.values():
    print(valor, end=' ')
  print('\n')

print('\n\n\n\n')
