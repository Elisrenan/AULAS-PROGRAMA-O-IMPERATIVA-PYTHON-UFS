
#tratamento de erros
while True:
  try:
    idade = int(input('Informe idade:'))
    break
  except ValueError:
    print('Erro de variavel, por favor digite uma informação válida!')

try:
  print(f'Sua idade é {idade}')
except NameError:
  print('Variavel não foi definida')