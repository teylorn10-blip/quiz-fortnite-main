perguntas= ('Qual a capital do brasil?','QUal a capital da paraiba?','Qual a capital de Minas gerais?')
respostas= ('brasilia','João pessoa','Belo Horizonte').lower() .strip()


for(pergunta) in (perguntas):
 respostas=input(pergunta)
if respostas == 'brasilia':
 print('acertou')
else:
 print('errou')