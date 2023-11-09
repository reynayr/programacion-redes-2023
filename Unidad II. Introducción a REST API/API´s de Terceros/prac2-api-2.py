'''
    Descripción: Generador de links
    Autor: Reyna Yazmin Ríos Martínez
    Fecha: 09/nov/2023
'''

import requests

while True:
    url = input("URL: ")
    if url.lower() == "quit" or url.lower() == "q":
        print("Gracias por usar el verificador de caché de URL")
        break

    main_api = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="
    
    # Construir la URL con el parámetro 'url'
    api_url = main_api + url

    # Realizar la solicitud a la API
    response = requests.get(api_url)

    # Convertir la respuesta a formato JSON
    json_data = response.json()

    # Imprimir la URL de la solicitud
    print("URL: " + api_url)

    # Verificar si la URL está en caché
    if 'id' in json_data and 'loadingExperience' in json_data['id']:
        print(f"La URL '{url}' está {'en caché' if json_data['id']['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['percentile'] > 0 else 'sin caché'}.")
    else:
        print(f"No se pudo determinar si la URL '{url}' está en caché.")

