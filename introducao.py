from statistics import mean

historia_n1 = float(input('Digite a primeira nota: '))
historia_n2 = float(input('Digite a segunda nota: '))

lista_notas = [historia_n1, historia_n2]
media = mean(lista_notas)
print(media)
# se
if media >= 7:
    print('aprovado')

# se não, se
elif media >= 5 and media < 7:
    print('Recuperação')

# caso contrário
else:
    print('Reprovado')