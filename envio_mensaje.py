import math  # Necesario para verificar NaN
import os
import requests
import urllib3
# Enviar mensaje a Teams via Power Automate
url_flujo = ""
payload = {
        "mensaje": " No está actualizado el reporte Consolidado store pickup del día de hoy.\nPor favor validar y actualizar el archivo. \nSaludos, "
    }
res = requests.post(url_flujo, json=payload, verify=False)
if res.status_code == 200:
  print("Mensaje enviado por Power Automate a Teams.")
else:
  print(f"Error al enviar mensaje: {res.status_code}\n{res.text}")
