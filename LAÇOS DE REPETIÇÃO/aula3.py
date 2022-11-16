#vai imprimir todos os números pares dado um determinado número pelo o úsuario, desde que, seja maior ou igual a dez
while True:
  try:
    numero = int(input("Informe um número maior ou igual a dez\n"))
    if numero >= 10:
      break
    else:
      print("O número digitado precisa ser maior ou igual a dez, por favor, digite novamente!")
  except ValueError:
    print("Valor inválido, digite novamente o número desejado.")

print("Utilizando o for")
for i in range(0, (numero + 1)):
  if i % 2 == 0:
    print(f"O número {i} é par")
  else:
    print(f"O número {i} é ímpar")

print("\nUtilizando o while")
controlador = 0
while controlador <= 10:
  if controlador % 2 == 0:
    print(f"O número {controlador} é par")
  else:
    print(f"O número {controlador} é ímpar")
  controlador += 1