'''
    Descripción: Generador de letras
    Autor: Reyna Yazmin Ríos Martínez
    Fecha: 09/nov/2023
'''

import urllib.parse
import requests

while True:
    title = input("Introduce tu canción: ")
    artist = input("Introduce el artista: ")
    
    if title == "quit":
        print("Adios")
        break
    
    main_api = 'https://api.lyrics.ovh/v1/artist/title'

    url = main_api + urllib.parse.urlencode({'title':title, 'artist':artist}) 

    json_data = requests.get(url).json()

    print("URL: " + (url))

    print(json_data['error'])