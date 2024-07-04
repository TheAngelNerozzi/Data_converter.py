import pandas as pd
import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

def convertir_archivo(tipo_archivo, nombre_archivo):
    with open('schema.avsc', 'r') as f: 
        schema = avro.schema.Parse(f.read())
    df = pd.read_csv(nombre_archivo) if tipo_archivo == "CSV" else pd.read_json(nombre_archivo, lines=True)
    df.to_parquet(nombre_archivo.replace(tipo_archivo, "parquet"), index=False)
    with DataFileWriter(open(nombre_archivo.replace(tipo_archivo, "avro"), 'wb'), DatumWriter(), schema) as writer:
        for _, row in df.iterrows():
            writer.append(dict(row))
    print("Archivo convertido a Parquet y Avro correctamente.")

# Ejecución del código
tipo_archivo = input("Ingresa el tipo de archivo (CSV o JSON): ")
nombre_archivo = input("Ingresa el nombre del archivo: ")
convertir_archivo(tipo_archivo, nombre_archivo)
