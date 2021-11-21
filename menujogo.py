menu = True
cabeçalho='------------------------------------------'
while menu == True:
    print(cabeçalho)
    print('\033[4;35;40mJOGO DA FORCA v1.0\033[m'.center(55))
    print(cabeçalho)
    print("\033[1;37mDigite o tema desejado\033[m".center(53))
    print("\033[1;35m1 - Animais")
    print('2 - Frutas')
    print("3 - Séries")
    print("4 - Filmes")
    print('5 - País\033[m')
    resposta=input()
    if(resposta == 'Animais' or resposta == 'Frutas' or resposta == 'Séries' or resposta == 'Filmes' or resposta == 'País'):
        menu=False
    else:
        print("\033[4;31m>>Tema não encontrado, digite novamente o tema desejado<<\033[m")
