'''
    Nombre: Reyna Yazmin Ríos Martínez
    Fecha: 01 / Dic / 2023
    Descripción: 2.6 - Lab NETCONF w/Python: List Capabilities 
'''
import ncclient
from ncclient import manager

m = manager.connect (
    host= '10.10.20.48',
    port= 830,
    username= 'developer',
    password= 'C1sco12345',
    hostkey_verify=False
)

print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)