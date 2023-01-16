def leArquivoSequencia (nomeArquivo):
    arq = open(nomeArquivo, "r")
    linha = arq.read()
    linha = list(linha.rstrip())
    linha.insert(0, '-')
    return(linha)

# Programa principal
lista_ori = leArquivoSequencia("sequence.txt")