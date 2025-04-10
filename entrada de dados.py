salario1= float     
salario2= float
nome1=  str    
nome2= str
idade= int 
media=float

print ('DADOS DA PRIMEIRA PESSOA')
nome1 = input ("Nome da primeira pessoa: ")
salario1 = float (input ("salário da primeira pessoa: R$ "))
idade= input ('Idade da primeira pessoa: ')

print ('DADOS DA SEGUNDA PESSOA')
nome2= input ("Nome da segunda pessoa: ")
salario2 = float (input ("salário da segunda pessoa: R$ "))
idade= input ('Idade da segunda pessoa: ')

media = (salario1 + salario2) / 2


print (f"Funcionário(a) {nome1}, recebe: R${salario1} e funcionário (a) {nome2}, recebe: R${salario2} e a média do pagamento deles é: {media}")
