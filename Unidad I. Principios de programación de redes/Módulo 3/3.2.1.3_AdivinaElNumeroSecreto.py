'''
 Nombre: Reyna Yazmin Ríos Martínez
 Fecha: 27/Septiembre/2023
 Laboratorio: 3.2.1.3
'''

secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
 
number = int(input())

while (number != secret_number):
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input())

print("¡Bien hecho, muggle! Eres libre ahora")