'''
    Descripción: Generador de links
    Autor: Reyna Yazmin Ríos Martínez
    Fecha: 09/nov/2023
'''

import requests

while True:
    breed = input("Raza de perro: ")
    if breed.lower() == "quit" or breed.lower() == "q":
        print("Gracias por usar la búsqueda de información sobre razas de perros")
        break

    main_api = "https://api.thedogapi.com/v1/breeds/search"
    
    # Construir la URL con el parámetro 'q' (query)
    api_url = f"{main_api}?q={breed}"

    # Realizar la solicitud a la API
    response = requests.get(api_url)

    # Convertir la respuesta a formato JSON
    json_data = response.json()

    # Imprimir la URL de la solicitud
    print("URL: " + api_url)

    # Verificar si se encontraron razas de perros
    if json_data:
        for result in json_data:
            print(f"Nombre de la raza: {result.get('name', 'No disponible')}")
            print(f"Descripción: {result.get('description', 'No disponible')}")
            print(f"Esperanza de vida: {result.get('life_span', 'No disponible')}")
            print("---")
    else:
        print(f"No se encontró información para la raza de perro '{breed}'.")
