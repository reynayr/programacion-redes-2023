'''
 Nombre: Reyna Yazmin Ríos Martínez
 Fecha: 29/Septiembre/2023
 Laboratorio: 3.2.1.10 
'''

palSinVocal = ""

userWord = input("Ingresa tu palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if letra == "A":
        continue
    elif letra== "E":
        continue
    elif letra== "I":
        continue
    elif letra== "O":
        continue
    elif letra== "U":
        continue
    else:
        print(letra)