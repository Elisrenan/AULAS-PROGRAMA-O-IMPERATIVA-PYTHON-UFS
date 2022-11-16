lista_dados = list()

x = int(
    input(
        "informe 1 para crescente, 2 para decrescente e 3 para o maior numero e 4 para o menor número.\n"
    ))

for i in range(3):
    aux_num = float(input("Informe um número:"))
    lista_dados.append(aux_num)

#obter o maior dentro de uma lista
maior = max(lista_dados)

#o menor dentro de uma lista
menor = min(lista_dados)

lista_em_ordem_crescente = []
lista_em_ordem_decrescente = []
lista_copia = []

#copiando uma lista antes de realizar alterações
lista_copia = lista_dados.copy()

#ordenando a lista em ordem crescente
lista_em_ordem_crescente = sorted(lista_dados)

#ordenando a lista em ordem decrescente
lista_em_ordem_decrescente = sorted(lista_dados, reverse=True)

if x == 1:
    print(f" em ordem crescente: {lista_em_ordem_crescente}")
elif x == 2:
    print(f" em ordem decrescente: {lista_em_ordem_decrescente}")
elif x == 3:
    print(f" O maior é: {maior}")
elif x == 4:
    print(f" O menor é: {menor}")
else:
    print("Houve algum erro tente novamente!")

#lista original
#print(lista_dados) 
#copia lista
#print(lista_copia)

#adicionando em um determinada posição especifica da lista
posicao = 1
numero = 10
lista_dados.insert(posicao, numero)

print("resultado da inserção usando o insert")
#lista original
print(lista_dados)

#copia lista
print(lista_copia)

#remover um elemento em uma posição especifica
posicao = 1
lista_dados.pop(posicao)

print("resultado da remoção usando o pop")
#lista original
print(lista_dados)

#copia lista
print(lista_copia)

#remover o ultimo elemento de uma lista
lista_dados.pop()

print("resultado da remoção usando o pop vazio")
#lista original
print(lista_dados)

#copia lista
print(lista_copia)

#remover o ultimo elemento de uma lista
elemento = 2.0
lista_dados.remove(elemento)

print("resultado da remoção usando o remove")
#lista original
print(lista_dados)

#copia lista
print(lista_copia)

#atualizando um elemento especifico
antigo_elemento = 5.0
posicao = lista_dados.index(antigo_elemento)
novo_elemento = 5.2
lista_dados.insert(posicao, novo_elemento)
lista_dados.remove(antigo_elemento)

print("resultado da atualização achando o elemento pelo index")
#lista original
print(lista_dados)

#copia lista
print(lista_copia)

#atualizando um elemento especifico
antigo_elemento = 5.0
novo_elemento = 5.2

qtd_elementos = len(lista_copia)
for i in range(qtd_elementos):
    if lista_copia[i] == antigo_elemento:
        posicao = i
        lista_copia.insert(posicao, novo_elemento)
        lista_copia.remove(antigo_elemento)
        break

print("resultado da atualização usando for i in range da lista copia")
#lista original
print(lista_dados)

#copia lista
print(lista_copia)
