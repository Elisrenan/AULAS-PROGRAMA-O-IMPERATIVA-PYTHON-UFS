import math

area =  float(input('Informe a area em m²'))

litros_nec = area / 3

latas_nec = math.ceil(litros_nec / 18)
valor = latas_nec * 80

print(f"Você irá precisar de {latas_nec} lata(s) e pagará o valor de R$ {valor}")