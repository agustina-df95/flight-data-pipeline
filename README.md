# Pipeline de Datos de Vuelos

## Descripción

Este proyecto implementa un pipeline de Ingeniería de Datos para la ingesta, procesamiento y almacenamiento de información de vuelos en tiempo real.

Los datos se obtienen mediante una API, se publican en Kafka, se procesan con Python y se almacenan en MongoDB y MinIO siguiendo una arquitectura basada en contenedores Docker.

## Tecnologías utilizadas

- Python
- Apache Kafka
- MongoDB
- MinIO
- Docker
- Docker Compose

## Estructura del proyecto

```
flight-data-pipeline/
├── data/
│   ├── bronze/
│   └── silver/
├── python/
│   ├── producer/
│   └── consumer/
├── schemas/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Funcionamiento

1. Obtención de datos de vuelos desde una API.
2. Publicación de los datos en Kafka mediante un productor.
3. Consumo y procesamiento de los mensajes con Python.
4. Almacenamiento de los datos procesados en MongoDB.
5. Gestión de archivos mediante MinIO.

## Ejecución

1. Clonar el repositorio.
2. Levantar los servicios con Docker Compose.
3. Ejecutar el productor.
4. Ejecutar el consumidor.
5. Verificar los datos almacenados en MongoDB y MinIO.
