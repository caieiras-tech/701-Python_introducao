"""
Desenvolva um algoritmo que leia o nome de um funcionário, número de horas trabalhadas e o valor que recebe por hora.
Como saída retorne o salário deste respectivo funcionário.
ex: Salário de Gabriel Roger:  R$ 399221.00
"""

nome = input('Nome funcionário: ')
qtd_hora = int(input('Digite a quantidade de horas trabalhadas de ' + nome + ': '))
valor_hora = float(input('Digite o valor hora de ' + nome + ': '))
sal = valor_hora * qtd_hora
print('Salário de ' + nome + ': R$' + str(sal))

