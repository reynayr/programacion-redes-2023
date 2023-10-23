'''
 Nombre: Reyna Yazmin Ríos Martínez
 Fecha: 29/Septiembre/2023
 Laboratorio: 3.2.1.15
'''

c0 = int(input("Dame un número: "))

pasos = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = int (c0 / 2)
        print(c0)
    else:
        c0 = int(3 * c0 + 1)
        print(c0)
    pasos += 1
    
print("Pasos:",pasos)