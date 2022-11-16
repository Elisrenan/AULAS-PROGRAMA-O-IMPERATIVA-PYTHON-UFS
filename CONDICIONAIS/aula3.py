#estrutura de bloco de condição com baixa peformace
altura = float(input("Informe sua altura: "))
genero = str(input("Digite M para Masculino ou F para Feminino"))

#pergunto ao python na linha 5 se genero for igual igual a M execute as linhas 6 e 7
if genero == 'M':
  pesoIdealhomem = float((72.7*altura) - 58)
  print(f"O peso ideal é: {pesoIdealhomem:.2f} Kg")
#pergunto ao python na linha 9 senão se o genero for igual igual a m execute as linhas 10 e 11
elif genero == 'm':
  pesoIdealhomem = float((72.7*altura) - 58)
  print(f"O peso ideal é: {pesoIdealhomem:.2f} Kg")
#pergunto ao python na linha 13 senão se o genero for igual igual a F execute as linhas 14 e 15
elif genero == 'F':
  pesoIdealmulher = float((62.1*altura) - 44.7)
  print(f"O peso ideal é: {pesoIdealmulher:.2f} Kg")
#pergunto ao python na linha 17 senão se o genero for igual igual a f execute as linhas 18 e 19
elif genero == 'f':
  pesoIdealmulher = float((62.1*altura) - 44.7)
  print(f"O peso ideal é: {pesoIdealmulher:.2f} Kg")
#senão nada do que foi perguntado no bloco de condição acima for verdade então execute a linha 22
else:
  print("Opção digita inválida!")

#estrura de bloco de condição com melhor peformace
altura = float(input("Informe sua altura: "))
genero = str(input("Digite M para Masculino ou F para Feminino"))

#se  genero for igual igual  M  ou o genero for igual igual a m execute as linhas 7 e 8
if genero == 'M' or genero == 'm':
  pesoIdealhomem = float((72.7*altura) - 58)
  print(f"O peso ideal é: {pesoIdealhomem:.2f} Kg")
#senão se o  genero for igual igual  F  ou o genero for igual igual a f execute as linhas 11 e 12
elif genero == 'F' or genero == 'f':
  pesoIdealmulher = float((62.1*altura) - 44.7)
  print(f"O peso ideal é: {pesoIdealmulher:.2f} Kg")
#senão as linas 6 e 10 não são verdades execute a linha 15
else:
  print("Opção digita inválida!")