import math

#fatorial
fact = math.factorial(5)

print(f"O fatorial de 5 é {fact}")

#somar dois ou mais numeros

soma = math.fsum([2,5])

print(f"A soma de 2 e 5 é = {soma:.0f}")

#raiz quadrada de um número
raiz = math.sqrt(25)
print(f"A raíz de 25 é = {raiz}")

#arredondar para cima ou para baixo, função nativa do python
num1 = round(10.5)
num2 = round(10.4)
num3 = round(10.6)
print("Função round")
print(f"num1 = {num1}\n num2 = {num2} \n num3 = {num3}")

#função da biblioteca math para arrendodar sempre para baixo
num1 = math.floor(10.5)
num2 = math.floor(10.4)
num3 = math.floor(10.6)
print("\nFunção math.floor")
print(f"num1 = {num1}\n num2 = {num2} \n num3 = {num3}")

#função da biblioteca math para arrendodar sempre para cima
num1 = math.ceil(10.5)
num2 = math.ceil(10.4)
num3 = math.ceil(10.6)
print("\nFunção math.ceil")
print(f"num1 = {num1}\n num2 = {num2} \n num3 = {num3}")