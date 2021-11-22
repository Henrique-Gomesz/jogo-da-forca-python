import os
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
Objeto=['faca','clipe','canivete','bacia','dado','grampo','garfo','quadro','anel','caderno','cadeira','escova','jaleco','urna','varal']
País=['brasil','bolivia','nigeria','argentina','angola','chile','china','cuba','dinamarca','japao','peru','paraguai','noruega','dinamarca','jamaica','russia','catar','equador']
Animal=['baleia','cachorro','gato','foca','flamingo','hiena','golfinho','raposa','vaca','tartaruga','zebra','urubu','ovelha','corvo','girafa','leao','cavalo','rato']
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
        print("\033[1;35m- Animal")
        print('- Frutas')
        print("- Objeto")
        print('- País\033[m')
        resposta=input()
        if(resposta == 'Animal' or resposta == 'Frutas' or resposta == 'Objeto'  or resposta == 'País'):
            menu=False
        else:
            os.system("cls")
            print("\033[4;31m>>Tema não encontrado, digite novamente o tema desejado<<\033[m")
            

    if(resposta == 'Animal'):
        palavra=random.choice(Animal)
    elif(resposta == 'Frutas'):
        palavra=random.choice(Frutas)
    elif(resposta == 'Objeto'):
        palavra=random.choice(Objeto)
    elif(resposta=='País'):
        palavra=random.choice(País)
    
    str= []
    for i in range(0,len(palavra)):
        str.append('_')
    cont=0
    acertou= False
    os.system("cls")
    #print(palavra)
    while cont!=6 and acertou==False:
        print(des_forca[cont])
        print(str)
        letra=input("\033[1;34mDigite uma letra:\033[m")
        letra=letra.lower()
        cont2=0
        if letra in lista_letras:
            os.system("cls")
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
                    os.system("cls")
                    print('\033[4;31mVocê Perdeu!\033[m')
                    print(des_forca[cont])
                    print(str)
                    print("Palavra:"+palavra.upper())
                    replay=input('\033[1;35mDeseja jogar novamente? (Y/N):\033[m')
                    replay=replay.upper()
                    if(replay == 'Y'):
                        jogo = True
                        menu = True
                        os.system("cls")
                    else:
                        jogo = False
                        os.system("cls")
                else:
                    os.system("cls")
                    print('\033[1;31mVocê errou, digite novamente!\033[m')
            else:
                os.system("cls")
                print("\033[4;32mParabéns, Você acertou!\033[m")
            acertou = True 

            for a in range(0,len(palavra)):
                if str[a]=="_":
                    acertou= False
            if(acertou == True):
                os.system("cls")
                print("\033[4;32mParabéns, Você venceu!\033[m")
                print(des_forca[cont])
                print(str)
                replay=input('\033[1;35mDeseja jogar novamente? (Y/N):\033[m')
                replay=replay.upper()
                if(replay == 'Y'):
                    jogo = True
                    menu = True
                    os.system("cls")
                else:
                    jogo = False
                    os.system("cls")
os.system("cls")
print(cabeçalho)
print("\033[4;36mCRÉDITOS\033[m".center(50))
print(cabeçalho)
print("\033[1;32mHenrique Gomes Junqueira".center(50))
print("Leonardo Gomes Anholetto".center(42))
print("Natanael Menezes".center(33))
print("Breno Queiroga".center(32))
print("Tauã\033[m".center(25))
print(cabeçalho)
