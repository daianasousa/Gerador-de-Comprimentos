from random import *

executa = True
masculino = [ "dag", "max", "fred" ]
feminino = ["meg", "lili", "pandora" ]

print("Serviço de escolha de nome para animais de estimação")
print("--------------------")


print('''
Menu
b = obter um nome macho
c = obter um nome femea
m = adicionar um nome M
f = adiciona um nome F
r = remover nome
p = imprimir hobbies
q = sair
''')

while executa == True:

    menuChoice = input("\n>_").lower()

    #'b' para receber um nome masculino
    if menuChoice == 'b':
        itemToAdd = int(input('Quantos nomes você precisa? '))
        b = itemToAdd
        #obtém um item ateatório da lista
        for rep in range(b):
            print( f'você deve chamar seu animal de estimação de {choice(masculino)}')


    #'c' para receber um nome feminino
    elif  menuChoice == 'c':
        itemToAdd = int(input('Quantos nomes você precisa? '))
        c = itemToAdd
        #obtém um item ateatório da lista
        for rep in range(c):
            print( f'você deve chamar seu animal de estimação de {choice(feminino)}')
            
    
    #'f' para adicionar um nome
    elif menuChoice == 'f':
        itemToAdd = input("Adicione um nome: ")
        if itemToAdd not in feminino:
            #adicione o código aqui..
            feminino.append(itemToAdd)

    #'m' para adicionar um nome
    elif menuChoice == 'm':
        itemToAdd = input("Adicione um nome: ")
        if itemToAdd not in masculino:
            #adicione o código aqui..
            masculino.append(itemToAdd)

    #'r' para remover um nome de ambas as listas
    elif menuChoice == 'r':

        itemToDelete = input("insira um nome a ser removido: ")
        #só remove um item se ele estiver na lista
        if itemToDelete in masculino:
            masculino.remove(itemToDelete)

        elif itemToDelete in feminino:
            feminino.remove(itemToDelete)
        else:
            print("O nome não está na lista!")

    #'p' para imprimir a lista de nomes
    elif menuChoice == 'p':
        print(masculino)
        print(feminino)

    #'q' para sair
    elif menuChoice == 'q':


        executa = False

    else:

        print("Insira uma opção válida!")