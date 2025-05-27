import requests
from math import radians, sin, cos, sqrt, atan2

async def calcular_distancia(cep_cliente: str, cep_prestador: str) -> float:
    def get_coordenadas(cep: str):
        url = f"https://nominatim.openstreetmap.org/search?postalcode={cep}&format=json&countrycodes=BR"
        headers = {"User-Agent": "MarketplaceSustentavel/1.0"}
        response = requests.get(url, headers=headers)
        data = response.json()
        if not data:
            raise ValueError("CEP não encontrado")
        return float(data[0]["lat"]), float(data[0]["lon"])

    try:
        lat1, lon1 = get_coordenadas(cep_cliente)
        lat2, lon2 = get_coordenadas(cep_prestador)
        R = 6371.0  # Raio da Terra em km
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distancia = R * c
        return distancia
    except:
        return 10.0  # Distância fictícia em caso de erro