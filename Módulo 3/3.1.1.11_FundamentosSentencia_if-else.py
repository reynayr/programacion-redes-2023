'''
 Nombre: Reyna Yazmin Ríos Martínez
 Fecha: 27/Septiembre/2023
 Laboratorio: 3.1.1.11
'''

income = float(input("Introduce el ingreso anual: "))

if (income < 85528):
    tax = (income * 0.18) - 556.02
elif (income > 85528):
    tax = 14839.02 + ((income - 85528)*0.32)

if tax < 0:
    tax = 0.0
    
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")