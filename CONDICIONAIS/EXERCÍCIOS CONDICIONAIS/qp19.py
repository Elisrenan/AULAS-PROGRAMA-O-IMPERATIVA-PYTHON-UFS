produto1 = float(input("Informe o preço do primeiro produto:R$"))
produto2 = float(input("Informe o preço do segundo produto:R$"))
produto3 = float(input("Informe o preço do terceiro produto:R$"))

if produto1 >= 0 and produto2 >= 0 and produto3 >= 0 :
  if produto1 < produto2 and produto1 < produto3 :
    print(f"O produto a ser comprado a partir do preço é {produto1}")
  elif produto2 < produto1 and produto2 < produto3 :
    print(f"O produto a ser comprado a partir do preço é {produto2}")
  elif produto3 < produto1 and produto3 < produto2 :
    print(f"O produto a ser comprado a partir do preço é {produto3}")
  else :
    print("Os três produtos possuem o mesmo preço")
else :
  print("Preço(s) inválido(s)")