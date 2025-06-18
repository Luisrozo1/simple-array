array_simple = [1,3,4,5,6,7,7,8,9,9,7,44,33,2,3,4,5,6,7]

potencia_de_3 =[]

def encontrar_potencia_de_3(lista):
    for numero in lista :
        numero = numero ** 3
        potencia_de_3.append(numero)         
    return lista

multiplos = encontrar_potencia_de_3(array_simple)

print(array_simple)
print(potencia_de_3)
 

  

 







  