def calcular_multa(aux_peso):
  aux_multa = 4
  aux_excesso = float()
  aux_valor_multa = float()
  if aux_peso > 50:
    aux_excesso = round(aux_peso - 50)
    aux_valor_multa = aux_multa * aux_excesso
  else:
    aux_valor_multa = 0.0
    
  return aux_valor_multa

def imprimir_multa(valor_multa):
  if valor_multa > 0:
    print(f"Você pagará R$ {valor_multa} de multa")
  else:
    print("Não existe multa!")
  
peso = float(input('informe o peso'))
imprimir_multa(calcular_multa(peso))

peso = float(input('informe o peso'))
imprimir_multa(calcular_multa(peso))
  
