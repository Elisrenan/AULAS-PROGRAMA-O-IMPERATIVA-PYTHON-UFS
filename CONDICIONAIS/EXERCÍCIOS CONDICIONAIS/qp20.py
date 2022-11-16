numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))
if numero1 > numero2 and numero1 > numero3:
  maior = numero1
  if numero2 > numero3:
    menor = numero3
    meio = numero2
  else:
    menor = numero2
    meio = numero3
elif numero2 > numero3:
  maior = numero2
  if numero3 > numero1:
    menor = numero1
    meio = numero3
  else:
    menor = numero3
    meio = numero1
else:
  maior = numero3
  if numero2 > numero1:
    menor = numero1
    meio = numero2
  else:
    menor = numero2
    meio = numero1
print(f"a ordem decrescente é {maior} {meio} {menor}")
