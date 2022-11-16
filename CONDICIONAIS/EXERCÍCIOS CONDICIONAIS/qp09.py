peso = float(input('informe o peso'))
excesso = float()
multa = 4
valor_total_multa = float()
if peso > 50:
  excesso = round(peso - 50)
  valor_total_multa = multa * excesso 
  print(f"Você pagará R$ {valor_total_multa} por exceder {excesso} Kg do pesso máximo.")
else:
  print("Não há multa!")