'''
 Nombre: Reyna Yazmin Ríos Martínez
 Fecha: 27/Septiembre/2023
 Laboratorio: 3.1.1.12
'''

year = int(input("Introduce un año: "))

if year < 1582:
    print("No está dentro del período del calendario Gregoriano")
if year % 4 != 0:
    print("Año común")
elif year % 100 != 0:
    print("Año bisiesto")
elif year % 400 != 0:
    print("Año común")
else:
    print("Año bisiesto")