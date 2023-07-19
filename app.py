import requests

# Hacer una solicitud GET a la API y almacenar la respuesta
response = requests.get(" https://api.covidtracking.com/v1/us/daily.json")
print(response.content)

# Verificar el estado de la respuesta
if response.status_code == 200:  # 200 significa que la solicitud fue exitosa
    # Acceder a los datos de la respuesta en formato JSON
    data = response.json()

    # Procesar los datos como desees
    # Por ejemplo, imprimir el contenido de la respuesta
    print(data)
else:
    # Si la solicitud no fue exitosa, mostrar un mensaje de error
    print("Error al realizar la solicitud:", response.status_code)
