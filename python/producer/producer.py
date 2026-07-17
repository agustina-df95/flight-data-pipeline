import os
import json
import requests
from dotenv import load_dotenv
from confluent_kafka import Producer

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

# Configuración de Kafka
producer = Producer({
    "bootstrap.servers": "kafka:9092"
})

# URL de AviationStack
URL = "https://api.aviationstack.com/v1/flights"

params = {
    "access_key": API_KEY,
    "limit": 10
}

print("Consultando AviationStack...")

response = requests.get(URL, params=params)

if response.status_code != 200:
    print(f"Error API: {response.status_code}")
    print(response.text)
    exit()

datos = response.json()

print(f"Vuelos recibidos: {len(datos.get('data', []))}")

for vuelo in datos.get("data", []):

    mensaje = {
        "flight_number": vuelo.get("flight", {}).get("iata"),
        "airline": vuelo.get("airline", {}).get("name"),
        "departure_airport": vuelo.get("departure", {}).get("iata"),
        "arrival_airport": vuelo.get("arrival", {}).get("iata"),
        "status": vuelo.get("flight_status"),
        "departure_time": vuelo.get("departure", {}).get("scheduled")
    }

    producer.produce(
        "flights",
        json.dumps(mensaje).encode("utf-8")
    )

producer.flush()

print("Mensajes enviados correctamente al topic 'flights'.")
