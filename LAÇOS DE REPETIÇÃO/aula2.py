#bloco while está sendo utilizado para validar a variavel número
while True:
  try:
    numero = int(input("Informe um número para calcular a tabuada de somar\n"))
    break
  except ValueError:
    print("Valor inválido, digite novamente o número desejado.")

print("Tabuada utilizando o while")
controlador = 0
while controlador < 10:
  controlador += 1
  soma = numero + controlador
  print(f"{numero} + {controlador} = {soma}")


print("Tabuada utilizando o for range de 1 até 10")
for i in range(1,11):
  soma = numero + i
  print(f"{numero} + {i} = {soma}")

print("Tabuada utilizando o for range até 10")
for i in range(10):
  n = i + 1
  soma = numero + n
  print(f"{numero} + {n} = {soma}")