nota1 = float(input("Informe a primeira nota"))
nota2 = float(input("Informe a segunda nota"))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
  media = (nota1 + nota2) /  2
  if media == 10:
    print("Aprovado com distinção")
  elif 7 <= media < 10:
    print("Aprovado")
  elif 0 <= media < 7:
    print("Reprovado")
else:
  print("Uma das notas digitadas é inválida!")