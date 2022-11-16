"""
Outros métodos muito importantes ao trabalhar com listas são o sort(), que ordena a lista, e o
reverse(), que inverte as posições dos itens. No caso da ordenação, ela será feita em ordem crescente
para números e em ordem lexicográfica para strings, ou seja, na forma como são ordenadas no
dicionário. A Listagem abaixo traz alguns exemplos de uso desses métodos.
"""
livros = ['Java', 'SqlServer', 'Delphi', 'Python',
'Android'] 
print('Antes do reverse: ',livros)
livros.reverse()
print('Depois do reverse como ficou: ',livros)
livros.sort()
print('Depois do sort que ordenou a lista como ficou: ',livros)

"""
Demais exemplos consulte o material de apoio
"""