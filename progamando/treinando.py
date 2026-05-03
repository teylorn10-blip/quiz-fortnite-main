
 #===PERGUNTAS EM LISTAS====

perguntas=('Qual e a cor da madeira?'),('Qual e a cor do ceu?'),('Qual a cor das arvores?')

respostas=('marron','azul','verde')

for pergunta,resposta_certa in zip(perguntas,respostas):
 resposta= input(pergunta)
 if resposta== resposta_certa:
    print ('acertou')
 else:
    print ('errou')
 