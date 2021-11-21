des_forca = ['''
 +---+
 |   |
     |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |    
=========
''']
import random
Filmes= []
Séries= []
País=['brasil','estados-unidos','africa-do-sul','argentina','angola','chile','coreia-do-norte','cuba','dinamarca','japao','peru','paraguai']
Animais=['baleia','cachorro','gato','foca','flamingo','hiena','golfinho','raposa','vaca','tartaruga','zebra','urubu','ovelha']
Frutas=['abacate','abacaxi','amora','banana','cacau','caqui','cereja','goiaba','framboesa','jaca','kiwi','laranja','manga','melancia','morango','pera','pitaya','tangerina','uva']
menu = True
jogo= True
cabeçalho='------------------------------------------'
while jogo == True:
    lista_letras=[]
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
        letra=input("\033[1;34mDigite uma letra:\033[m")
        letra=letra.lower()
        cont2=0
        if letra in lista_letras:
            print("\033[1;33mPalavra repetida, digite novamente!\033[m") 
        else:
            lista_letras.append(letra)
            for i in range(0,len(palavra)):
                if letra==palavra[i]:
                    str[i]=letra
                    cont2+=1
            if cont2==0:
                cont+=1
                if(cont == 6):
                    print(des_forca[cont])
                    print('\033[4;31mVocê Perdeu!\033[m')
                    replay=input('\033[1;35mDeseja jogar novamente? (Y/N):\033[m')
                    replay=replay.upper()
                    if(replay == 'Y'):
                        jogo = True
                        menu = True
                    else:
                        jogo = False
                print(des_forca[cont])
                print('\033[1;31mVocê errou, digite novamente!\033[m')
                
            print(str)
            acertou = True 

            for a in range(0,len(palavra)):
                if str[a]=="_":
                    acertou= False
            if(acertou == True):
                print("\033[4;32mParabéns, Você venceu!\033[m")
                replay=input('\033[1;35mDeseja jogar novamente? (Y/N):\033[m')
                replay=replay.upper()
                if(replay == 'Y'):
                    jogo = True
                    menu = True
                else:
                    jogo = False
            