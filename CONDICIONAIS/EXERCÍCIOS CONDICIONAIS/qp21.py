turno=str(input("Em qual turno você estuda? Digite M para matutina, V para vespertino ou N para noturno.\n")).capitalize()

if turno=="M":
  print("\n Bom dia!")
elif turno=="V":
  print ("\n Boa tarde!")
elif turno=="N":
  print ("\n Boa noite!")
else:
  print("Dígito inválido!")