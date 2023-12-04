'''
    Nombre: Reyna Yazmin Ríos
    Fecha: 04 / Dic / 2023
    Descripción: Lab 2.8 NETCONF w/Python: Device Configuration
    Parte 1
'''

from ncclient import manager
import xml.dom.minidom

m = manager.connect (
    host='10.10.20.48',
    port=830,
    username='developer',
    password='C1sco12345',
    hostkey_verify=False
)

netconf_reply = m.get_config(source="running")
print(netconf_reply)

print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )