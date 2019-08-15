import random
lista = []
i = 0
qtd = int(input('digite a qtd de itens da lista: '))
while i <= qtd:
    lista.append(random.randrange(1,1000,3))
    i += 1

print(max(lista))
print(min(lista))

