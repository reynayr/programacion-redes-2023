'''
  Nombre: Reyna Yazmin Ríos Martínez
  Fecha: 23 / Oct /2023
  Descripción: Imporatando API
'''

import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    print("Hasta luego querido viajero")

    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "YW0ScRakZg1x3d8xSLUvJlD7by2jQEW9"

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
      print("API Status: " + str(json_status) + " = A successful route call.\n")
    elif json_status != 0:
      print("API Status: " + str(json_status) + " = A failure route call.\n")
