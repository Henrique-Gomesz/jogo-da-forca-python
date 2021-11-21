import random
Filmes=[]
Séries=[]
País=['brasil','estados-unidos','africa-do-sul','argentina','angola','chile','coreia-do-norte','cuba','dinamarca','japao','peru','paraguai']
Animais=['baleia','cachorro','gato','foca','flamingo','hiena','golfinho','raposa','vaca','tartaruga','zebra','urubu','ovelha']
Frutas=['abacate','abacaxi','amora','banana','cacau','caqui','cereja','goiaba','framboesa','jaca','kiwi','laranja','manga','melancia','morango','pera','pitaya','tangerina','uva']
menu = True
cabeçalho='------------------------------------------'
while menu == True:
    print(cabeçalho)
    print('\033[4;35;40mJOGO DA FORCA v1.0\033[m'.center(55))
    print(cabeçalho)
    print("\033[1;37mDigite o tema desejado\033[m".center(53))
    print("\033[1;35m- Animais")
    print('- Frutas')
    print("- Séries")
    print("- Filmes")
    print('- País\033[m')
    resposta=input()
    if(resposta == 'Animais' or resposta == 'Frutas' or resposta == 'Séries' or resposta == 'Filmes' or resposta == 'País'):
        menu=False
    else:
        print("\033[4;31m>>Tema não encontrado, digite novamente o tema desejado<<\033[m")

if(resposta == 'Animais'):
    palavra=random.choice(Animais)
elif(resposta == 'Frutas'):
    palavra=random.choice(Frutas)
elif(resposta == 'Séries'):
    palavra=random.choice(Séries)
elif(resposta == 'Filmes'):
    palavra=random.choice(Filmes)
elif(resposta=='País'):
    palavra=random.choice(País)

print(palavra)
str= []
for i in range(0,len(palavra)):
    str.append('_')
print(str)
cont=0
acertou= False
while cont!=6 and acertou==False:
    letra=input("Digite uma letra:")
    cont2=0
    for i in range(0,len(palavra)):
        if letra==palavra[i]:
            str[i]=letra
            cont2+=1
    if cont2==0:
        cont+=1
    print(str)
    acertou = True 

    for a in range(0,len(palavra)):
        if str[a]=="_":
            acertou= False
            