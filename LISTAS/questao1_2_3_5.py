lista_numeros = list()

def validar_numero(aux_numero):
  valido = True
  try:
    aux_numero = float(aux_numero)
  except:
    valido = False
    print('Número inválido digite novamente')
  return valido

def inserir_numero(aux_numero):
  inseriu = False
  if validar_numero(aux_numero):
    inseriu = True
    lista_numeros.append(float(aux_numero))
  return inseriu  

def ordenar_lista():
  lista_numeros.sort()

def inverter_lista():
  lista_numeros.reverse()

def calcular_media_numeros():
  media = 0
  total_soma = sum(lista_numeros)
  qtd_numeros = len(lista_numeros)
  media = total_soma / qtd_numeros
  return media
  
def imprimir_lista_sem_formatacao():
  print(lista_numeros)

def imprimir_lista_formatada():
  texto = 'O resultado é:\n'
  for numero in lista_numeros:
    texto = texto +str(numero)+'\n'
  print(texto)

def qtd_numeros():
  return len(lista_numeros)
  
def gerar_lista_numeros_pares_e_impares():
  lista_pares = list()
  lista_impares = list()
  for numero in lista_numeros:
    if numero % 2 == 0:
      lista_pares.append(numero)
    else:
      lista_impares.append(numero)
  print('Números pares:\n', lista_pares)
  print('Números ímpares:\n', lista_impares)
  
#teste 
qtd_repeticoes = int(input("Informe quantas vezes deseja repetir o cadastro de números."))

for i in range(qtd_repeticoes):
  numero = input('Informe um número:')
  while True:
    if inserir_numero(numero):
      break
    else:
      numero = input('Informe um número:')

#primeira questão
#print('Resultado questão 1')
#imprimir_lista()

#segunda questão
#print('Resultado questão 1')
#ordenar_lista()
#inverter_lista()
#imprimir_lista()

#terceira questão
#imprimir_lista_formatada()
#print(f"A média do aluno foi de {calcular_media_numeros()}")

#quinta questão
#gerar_lista_numeros_pares_e_impares()
