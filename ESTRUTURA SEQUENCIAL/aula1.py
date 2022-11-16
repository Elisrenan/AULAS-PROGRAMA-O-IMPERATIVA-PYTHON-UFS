#saída de dados
print('Hello World!')

#declarações de variaveis simples
idade = int()
salario = float()
nome = str()
possui_dinheiro = bool()

#variaveis explicitas - atribuindo valores
idade = 27
salario = 1000.00
nome = "Elisrenan Barbosa"
possui_dinheiro = True

#sintaxe de saída simples
print(idade)
print(salario)
print(nome)
print(possui_dinheiro)

#sintaxe de saída, print com virgula 
print("Nome: ", nome)
print("Idade: ", idade)
print("Salario: ", salario)
print("Possui Dinheiro? ", possui_dinheiro)

#sintaxe de saída, print formatado com f linha
print(f"\n\nNome: {nome} \n Idade: {idade} \n Salário: {salario} \n Possui Dinheiro? {possui_dinheiro}")

#criar variaveis implicitas e solicitando com o input
idade = int(input("Informe sua idade:\n"))
salario = float(input("Informe seu salario:\n"))
nome = str(input("Informe seu nome:\n"))
possui_dinheiro = bool(input("Possui dinheiro?:\n"))

#sintaxe de saída, print formatado com format
print("\n\nNome: {} \n Idade: {} \n Salário: {} \n Possui Dinheiro? {}".format(nome, idade, salario, possui_dinheiro))

