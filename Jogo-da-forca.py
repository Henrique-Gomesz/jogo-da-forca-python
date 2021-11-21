import random
print("-------------------------")
print('\033[1;35m'+'Escolha o tema para jogar'+'\033[0;0m')



pais=['brasil','estados-unidos','africa-do-sul','argentina','angola','chile','coreia-do-norte','cuba','dinamarca','japao','peru','paraguai']
animais=['baleia','cachorro','gato','foca','flamingo','hiena','golfinho','raposa','vaca','tartaruga','zebra','urubu','ovelha']
frutas=['abacate','abacaxi','amora','banana','cacau','caqui','cereja','goiaba','framboesa','jaca','kiwi','laranja','manga','melancia','morango','pera','pitaya','tangerina','uva']
palavra=random.choice(frutas)
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
            