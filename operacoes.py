file = open('home/cimara/Documentos/PLP/Atv02/DirShell01/operacoes.txt', 'w+')
num1 = 0
num2 = 0
opcao = ''
resultado = 0
num1 = int(input('Informa um numero: '))
opcao = input('Informe a operação +, -, /, * ')
num2 = int(input('Informa um numero: '))

if opcao == '+':
   resultado = num1 + num1
elif opcao == '-':
   resultado = num1 - num1
elif opcao == '*':
   resultado = num1 * num1  
elif opcao == '/':
   resultado = num1 / num1  
else: 
   resultado = 'opcao Inválida!'
   
print (num1 + '' + opcao + '' +  num2 + ' = '+ resultado)   
   
