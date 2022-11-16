#primeira questão
import math

raio = float(input("Informe o raio"))

area = math.pi * (raio**2)

print(f"A area de um circulo de raio {raio} é igual {area:.2f}") 

#segunda questão 
lado = float(input("Informe o lado do quadrado: "))

area = lado * lado

print(f"A area de um quadrado com lado {lado} é igual a {area:.2f}")

#questão 3
#recebe o valor da hora trabahada
vl_hora = float(input("Quanto você ganha por hora? "))

#recebe a quantidade de horas trabalhadas
qtd_horas = int(input("Quantas horas você trabalhou no mês?"))

salario = vl_hora * qtd_horas

print(f"Seu salário neste mês é de: {salario}")

#QUARTA
F = float(input("Informe os graus Farenheit:"))
C = (5 * (F-32) / 9)
print(f"Os graus Farenheit {F:.2F} em Celsius é igual a {C:.2F}")

#5 QUESTÃO
c = float(input("Informe a temperatura em celsius:"))
f = c * 1.8 + 32
print (f"A temperatura em fahrenheit é:{f:.2f}")

#6 questão
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))

conta1 = (numero1 * 2) + (numero2 / 2)

print(f"O dobro do primeiro número com a metade do segundo número é {conta1} ")

conta2 = numero1*3 + numero3

print(f"a soma do triplo do primeiro numero com o terceiro numero e {conta2}")

#C
Cubo = numero3 ** 3
print(f" O CUBO {Cubo}")

#questão 7
altura = float(input("Informe sua altura: "))
pesoIdeal = float((72.7*altura) - 58)
print(f"Seu peso ideal e {pesoIdeal:.2f}")

#questão 8
altura = float(input("Informe sua altura: "))
pesoIdealhomem = float((72.7*altura) - 58)
pesoIdealmulher = float((62.1*altura) - 44.7)

print(f"Se for homem o peso ideal é: {pesoIdealhomem:.2f} Kg")

print(f"Se for mulher o peso ideal é: {pesoIdealmulher:.2f} Kg")

