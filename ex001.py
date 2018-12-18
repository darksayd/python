
nome = input('Qual o seu nome: ')
print('Prazer em te conhecer {:=^60}!'.format(nome))

n1 = int(input('digite um valor: '))

if n1 <= 20:
    print('este valor é menor ou igual a 20')
elif n1 > 20:
    print('esse valor é maior que 20!!!')
else:
    print('Valor informado com sucesso!!! ');

    print('o valor digitado é {}'.format(n1), type(n1))

n3 = int(145)
n4 = int(n1*n3)
print('o valor digitado multiplicado por 145 é igual a: {} '.format(n4), type(n4))

n2 = str(n1)
print('o valor é um valor numérico ', n2.isnumeric())
print('o valor é um valor decimal ', n2.isdecimal())
print('o valor é um é um numero ', n2.isalnum())
print('o valor é um valor alphanumérico ', n2.isalpha())
# utilizando a instrução IF e ELSE
if n2.isnumeric:
    print('o sistema está sendo criado')
else:
    print('o sistema está bugado')
n5 = int(input('entre com um valor: '))
print('o valor digitado é: {}'.format(n5))
# aprendendo a utilizar a instrução FOR
n6 = ['Alunos ADM: Adriana e brenda', 'aluno TI: Junior e thiago', 'ED.Física: Sheila e Juliana']
for n in[n6]:
    print(n)

    print('Todos os alunos fora listados com sucesso!!')
# utilizando variaveis do tipo booleano
a = bool(input('entre com um valor: '))
print(' o valor inserido é: ', a)
n1 = int(input('digite um valor: '))
n2 = int(input('digte um valor: '))
s = n1+n2
mult = n1*n2
div = n1/n2
di = n1//n2
ex = n1**n2
print('a soma é {},\n a multiplicação é {}, a divisaão é {:.3f}'.format(s, mult, div), end=' ')
print('a divisão por inteira é {}, a exponenciação é {} '.format(di, ex), end='\n \n  Inicio da atualização do arq.txt\n')
#bloco para abrir um arquivo e ler e atualizar um arquivo .txt
pad = open("D:\DevOps\python.txt","+r",)
pads = pad.read() #este método lê todo o arquivo já o método readlines faz a leitura linha por linha
# e apresenta dentro de chave em formato de lista
print(pads)
pads = str(input('digite as atualizações do arquivo: \n \n'))
pad.write(pads)
pad.close()

with open("D:\DevOps\python.txt") as arquivo:
    tudo = arquivo.read()
print(tudo)










       
