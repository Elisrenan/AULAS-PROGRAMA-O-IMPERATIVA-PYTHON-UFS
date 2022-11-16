letra = str(input("Informe uma letra")).capitalize()

if len(letra) == 1:
  if letra == "A" or letra == "E" or letra =="I" or letra == "O" or letra == "U":
    print("A letra digitada é uma vogal")
  else:
    print("A letra digitada é uma consoante")
else:
  print("Letra inválida")