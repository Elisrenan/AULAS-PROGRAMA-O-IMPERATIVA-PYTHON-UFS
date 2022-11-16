lista_letras = list()

def verifica_se_string(letra):
  valido = False
  try:
    aux_numero = float(letra)
    print('Não é uma letra digite novamente')
  except:
    valido = True
  return valido

def verifica_se_letra(letra):
  valido = False
  lista_letras_aux = ['A', 'B', 'C', 'D', 'E', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'Y', 'V', 'W']
  for letra_aux in lista_letras_aux:
    if letra == letra_aux:
      valido = True
      break  

  if valido == False:
    print('Não é uma letra digite novamente')
  return valido
  
def inserir_letra(letra):
  inseriu = False
  if verifica_se_string(letra):
    if verifica_se_letra(letra):
      inseriu = True
      lista_letras.append(letra)
  return inseriu 

def verificar_consoantes():
  qtd_consoantes = 0
  for letra in lista_letras:
    if letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U':
      qtd_consoantes += 1

  print(f"Existem {qtd_consoantes} consoantes cadastradas")
  
#teste 
qtd_repeticoes = int(input("Informe quantas vezes deseja repetir o cadastro de letras."))

for i in range(qtd_repeticoes):
  letra = input('Informe uma letra:')
  while True:
    letra = letra.upper()
    if inserir_letra(letra):
      print("Letra cadastrada com sucesso!")
      break
    else:
      letra = input('Informe uma letra:')

print(lista_letras)
verificar_consoantes()