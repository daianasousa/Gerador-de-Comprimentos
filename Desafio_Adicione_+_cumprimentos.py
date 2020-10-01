from random import *

print("Gerador de Cumprimentos")
print("--------------------")

adjetivos = [ "maravilhoso", "acima da média", "excelente" , "muito bom", "perfeito", "magnifico" ]
hobbies = [ "anda de bicicleta", "programar", "fazer chá", "comer" ]

nome = input("Qual é o seu nome?: ")
print( "Aqui está o seu cumprimento" , nome , ":" )

#obtém um item aleatório de ambas as listas e adiciona-os ao cumprimento
print( nome , "você é" , choice(adjetivos) , "em" , choice(hobbies) )
print( "De nada!" )