import math
area = float(input('Informe a area em m²:\n'))

if area > 0:
  litros_nec = area / 6
  litros_mais_dez_porc = litros_nec + (litros_nec * 0.1)
  litros_mais_dez_porc = round(litros_mais_dez_porc, 2)

  #calculo lata - resposta letra A
  lata_nec = litros_mais_dez_porc / 18
  lata_nec_arredondada = math.ceil(lata_nec)
  custo_lata = lata_nec_arredondada * 80
  #print(lata_nec)
  print(f"\nPara a área de {area}m² você irá precisar de {litros_mais_dez_porc} litros, o que equivale a {lata_nec_arredondada} latas de tinta, com um custo total de R$ {custo_lata},00.")

  #calculo galão - respota letra B
  galao_nec = litros_mais_dez_porc / 3.6
  galao_nec_arredondada = math.ceil(galao_nec)
  custo_galao = galao_nec_arredondada * 25
  #print(galao_nec)
  print(f"\nPara a área de {area}m² você irá precisar de {litros_mais_dez_porc} litros, o que equivale a {galao_nec_arredondada} galões de tinta, com um custo total de R$ {custo_galao},00.")

  #calculo lata e galão - respota letra c
  lata_litros_nec = litros_mais_dez_porc // 18
  galoes_litros_nec = math.ceil((litros_mais_dez_porc % 18) / 3.6)

  custo_lata_galao = (lata_litros_nec * 80) + (galoes_litros_nec * 25)
  print("=================================================")
  if custo_galao <= custo_lata and custo_galao <= custo_lata_galao:
    print(f"\nPara a área de {area}m² você irá precisar de {litros_mais_dez_porc} litros, o ideal é que você compre apenas {galao_nec_arredondada} galões de tinta, com um custo total de R$ {custo_galao},00.")
  elif custo_lata <= custo_galao and custo_lata <= custo_lata_galao:
    print(f"\nPara a área de {area}m² você irá precisar de {litros_mais_dez_porc} litros, o ideal é que você compre apenas {lata_nec_arredondada} latas de tinta, com um custo total de R$ {custo_lata},00.")
  elif custo_lata_galao <= custo_galao and custo_lata_galao <= custo_lata:
    print(f"\nPara a área de {area}m² você irá precisar de {litros_mais_dez_porc} litros, o ideal é que você compre {lata_litros_nec} latas e {galoes_litros_nec} galões de tinta, com um custo total de R$ {custo_lata_galao}0.")
else:
  print("Área inválida!")