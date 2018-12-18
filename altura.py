

#programa multa

def hello(meu_nome):
    print('Seja bem vindo ',meu_nome)

def gravar(salva):
    pad = open("D:\DevOps\python.txt", "+r", )
    pads = pad.read()  # este método lê todo o arquivo já o método readlines faz a leitura linha por linha
    
    print(pads)
    pads = str(input('digite as atualizações do arquivo: \n \n'))
    pad.write(pads)
    pad.close()

  



