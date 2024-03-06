import json
from datetime import datetime, timedelta
import random

# Función para formatear la fecha y hora
def format_timestamp(timestamp):
    return timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")

# Configuración inicial
start_timestamp = datetime(2024, 1, 1, 0, 1, 0)
json_objects = []

for i in range(100000):
    current_timestamp = start_timestamp + timedelta(minutes=i)
    success_value = random.choice([True, False])
    label_value = random.choice(["Obtener clientes", "Obtener propiedades", "Autenticarse", "Cerrar sesión"])
    response_time_value = random.randint(100, 5000)
    usuarios_conectados_value = random.randint(1, 10000)
    tiempo_carga_pagina_value = random.randint(100, 5000)
    tasa_errores_value = round(random.uniform(0, 1), 2)

    json_objects.append({
        "index": {},
    })
    json_objects.append({
        "@timestamp": format_timestamp(current_timestamp),
        "label": label_value,
        "responseTime": response_time_value,
        "success": success_value,
        "data": {
            "usuariosConectados": usuarios_conectados_value,
            "tiempoCargaPagina": tiempo_carga_pagina_value,
            "tasaErrores": tasa_errores_value
        }
    })

# Convertir la lista de objetos JSON a una cadena JSON sin saltos de línea
json_data = "\n".join(json.dumps(obj, separators=(',', ':')) for obj in json_objects)

# Imprimir la cadena JSON generada
print(json_data)
