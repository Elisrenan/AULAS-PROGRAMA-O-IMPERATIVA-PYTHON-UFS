idade = int(input("Informe a idade"))

if idade > 0 and idade <= 11:
  print("Tu é uma criança")
elif idade >= 12 and idade <= 17:
  print("Tu é um adolescente")
elif idade >= 18 and idade <= 24:
  print("Tu é um jovem")
elif idade >= 25 and idade <= 60:
  print("Tu é um adulto")
elif idade > 60:
  print("Tu é um idoso")
else:
  print("número digitado inválido")