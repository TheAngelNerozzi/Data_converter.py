# CSV and JSON to Parquet and Avro Converter

This Python script makes it easy to convert CSV and JSON files to formats optimised for data analysis, such as Parquet and Avro.

## Overview

The data_converter.py script provides an easy way to transform CSV and JSON files to Parquet and Avro. The output formats are ideal for large-scale data storage and processing, especially in distributed analytics environments such as Hadoop or Spark.

## Installation

1. Install Python 3: Make sure you have Python 3 installed on your system. You can download it from [https://www.python.org/](https://www.python.org/).

2. Install dependencies: Use pip to install the necessary libraries:

   `bash
   pip install pandas avro-python3

## Use

1. Save the script: Save the data_converter.py file in the same directory as the CSV or JSON files you want to convert, along with the schema.avsc file.

2. Run the script: Open a terminal or command line and run the script:

3. Interaction with the script: The script will prompt you for the following:
Input file type: Enter "CSV" or "JSON".
Input file name: Enter the name of the file, including the file extension (e.g. "data.csv" or "data.json").

4. Output: The script will create two output files in the same directory:
Parquet file: With the extension ".parquet" (e.g. "data.parquet").
Avro file: With the extension ".avro" (e.g. "data.avro").

## Avro scheme

The script uses a predefined Avro schema for Avro conversion. The schema is defined in the schema.avsc file. 

Example of schema.avsc:

{
  "tipo": "registro",
  "nombre": "Datos",
  "fields": [
    {"name": "campo1", "tipo": "cadena"},
    {"name": "field2", "type": "int"},
    {"name": "field3", "type": "double"},
    {"name": "field4", "type": "string"}
  ]
} 




