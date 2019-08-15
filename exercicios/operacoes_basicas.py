def calcula_geral(valor1, valor2, operacao):
    calc = (valor1) + operacao + (valor2)
    return calc

valor1 = float(input('digite o valor1: '))
valor2 = float(input('digite o valor2: '))
operacao = input('digite a operação')

calc = calcula_geral(valor1, valor2, operacao)
print('resultado: ' + str(calc))