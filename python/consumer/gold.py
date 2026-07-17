import pandas as pd
from pymongo import MongoClient

# Leer Silver
df = pd.read_csv("/app/data/silver/flights_silver.csv")

# Transformación Gold
gold = (
    df.groupby("airline")
      .size()
      .reset_index(name="total_flights")
)

# Conexión a MongoDB
cliente = MongoClient("mongodb://mongodb:27017/")
db = cliente["flight_db"]
coleccion = db["gold"]

# Limpiar colección
coleccion.delete_many({})

# Guardar datos
coleccion.insert_many(gold.to_dict("records"))

print("Capa Gold creada correctamente en MongoDB.")
