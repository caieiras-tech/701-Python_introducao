
dicionario_de_dias = {
    1: 'dom',
    2: 'seg',
    3: 'ter',
    4: 'qua',
    5: 'qui',
    6: 'sex',
    7: 'sab'
}



dia = int(input('digite o dia da semana de 1 a 7: '))

try:
    print(dicionario_de_dias[dia])
except:
    print('OPS')
