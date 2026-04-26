# painel login

print('==================')
print(' QUIZ FORTNITE 🎮 ')
print('==================')

nome= ''
while nome== '':
  nome= input('Digite seu nome?').strip()
print ('Seja bem vindo ao quiz!', nome)

pontos= 0

#=== pergunta 1===
pergunta = ''

while pergunta != '2017':
    pergunta = input('Em que ano o Fortnite Battle Royale foi fundado? ').strip()
    
    if pergunta != '2017':
        print('errou')
        pontos +=1
print('acertou')



# === pergunta 2===


pergunta= input('Qual e a primeira skin do fortnite battle royale?').strip().lower()
if pergunta=='renegade':
 print('acertou')
 pontos +=2
else :
 print('errou')


 # === pergunta 3===

 
pergunta= input('Qual foi o primeiro player a ganhar o mundial de Fortnite?') .strip().lower()

resposta= ('bugha')

if pergunta==('bugha'):
  print('acertou')
  pontos +=3
else:
  print('errou')


  #=== Pergunta 4===

  
pergunta= input('Qual e o melhor jogador de Fortnite do mundo?').strip().lower()

resposta= ('peterbot')

if pergunta==('peterbot'):
 print('acertou')
 pontos +=4
else:
 print('errou')


 #=== pergunta 5====


pergunta= input( 'Em que capitulo ocorreu o evento do travis scott?' ).strip().lower()

resposta= ('capitulo 2','2')

if pergunta in ('capitulo 2','2'):
 print ('acertou')
 pontos +=5
else:
 print ('errou')



 #Resultado final
print(f'voce fez {pontos} pontos')