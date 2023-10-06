'''
 Nombre: Reyna Yazmin Ríos Martínez
 Fecha: 29/Septiembre/2023
 Laboratorio: 3.2.1.14
'''

blocks = int(input("Ingresa el número de bloques: "))

height = 0
step = 1

while blocks > height:
    height += 1
    blocks -= height
    
print("La altura de la pirámide:", height)