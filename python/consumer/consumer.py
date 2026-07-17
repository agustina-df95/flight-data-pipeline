import json
import os

import pandas as pd
from confluent_kafka import Consumer
from pymongo import MongoClient

# MongoDB
cliente = MongoClient("mongodb://mongodb:27017/")
db = cliente["flight_db"]
coleccion = db["bronze"]

# Kafka
conf = {
    "bootstrap.servers": "kafka:9092",
    "group.id": "flight-consumer",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(conf)
consumer.subscribe(["flights"])

# Carpeta para CSV
os.makedirs("/app/data/bronze", exist_ok=True)

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    vuelo = json.loads(msg.value().decode("utf-8"))

    print("Vuelo recibido")
    print(vuelo)

    # Guardar en MongoDB
    coleccion.insert_one(vuelo)

    # Guardar en CSV
    df = pd.DataFrame([vuelo])

    archivo = "/app/data/bronze/flights.csv"

    if os.path.exists(archivo):
        df.to_csv(archivo, mode="a", header=False, index=False)
    else:
        df.to_csv(archivo, index=False)
