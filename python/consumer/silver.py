import os
import pandas as pd

entrada = "/app/data/bronze/flights.csv"
salida = "/app/data/silver"

os.makedirs(salida, exist_ok=True)

df = pd.read_csv(
    entrada,
    usecols=[0,1,2,3,4,5],
    names=[
        "flight_number",
        "airline",
        "departure_airport",
        "arrival_airport",
        "status",
        "departure_time"
    ],
    header=0
)

# Eliminar duplicados
df = df.drop_duplicates()

# Eliminar filas completamente vacías
df = df.dropna(how="all")

# Convertir fecha
if "departure_time" in df.columns:
    df["departure_time"] = pd.to_datetime(
        df["departure_time"],
        errors="coerce"
    )

df.to_csv(f"{salida}/flights_silver.csv", index=False)

print("Capa Silver creada correctamente.")
