import requests

API_KEY = "3b30ee6b-9e79-4e0f-86fb-595a9cba352a"

def get_coords(ciudad):
    url = "https://graphhopper.com/api/1/geocode"
    params = {
        "q": ciudad,
        "locale": "es",
        "key": API_KEY
    }
    r = requests.get(url, params=params).json()
    if r['hits']:
        lat = r['hits'][0]['point']['lat']
        lng = r['hits'][0]['point']['lng']
        return f"{lat},{lng}"
    else:
        print(f"❌ No se encontró la ciudad: {ciudad}")
        return None

def obtener_datos(origen_nombre, destino_nombre):
    origen_coords = get_coords(origen_nombre)
    destino_coords = get_coords(destino_nombre)

    if not origen_coords or not destino_coords:
        return

    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [origen_coords, destino_coords],
        "vehicle": "car",
        "locale": "es",
        "instructions": "true",
        "key": API_KEY
    }

    r = requests.get(url, params=params).json()
    if 'paths' not in r:
        print("❌ No se encontró una ruta válida.")
        return

    distancia_km = r['paths'][0]['distance'] / 1000
    duracion_seg = r['paths'][0]['time'] / 1000
    litros = distancia_km / 12

    print(f"\nDistancia: {distancia_km:.2f} km")
    print(f"Duración: {int(duracion_seg//3600)}h {int((duracion_seg%3600)//60)}m {int(duracion_seg%60)}s")
    print(f"Combustible estimado: {litros:.2f} L\n")
    print("Narrativa:")
    for paso in r['paths'][0]['instructions']:
        print("-", paso['text'])

# Programa principal
print("Presiona 'q' para salir.")
while True:
    origen = input("Ciudad de Origen: ")
    if origen.lower() == "q":
        break
    destino = input("Ciudad de Destino: ")
    if destino.lower() == "q":
        break
    obtener_datos(origen, destino)
app.run(host="0.0.0.0", port=9999)
