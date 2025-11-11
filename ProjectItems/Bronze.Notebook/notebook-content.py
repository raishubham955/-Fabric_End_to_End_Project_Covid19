# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "6e283668-4dcb-4086-8f6a-120429db5288",
# META       "default_lakehouse_name": "Demo",
# META       "default_lakehouse_workspace_id": "513d0a6d-98c3-4b8f-a54c-28abe377f164",
# META       "known_lakehouses": [
# META         {
# META           "id": "6e283668-4dcb-4086-8f6a-120429db5288"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

import requests
import json
from pyspark.sql import SparkSession

url = "https://disease.sh/v3/covid-19/countries"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

# Save JSON to a file in lakehouse file section

    file_path = '/lakehouse/default/Files/Covid_bronze.json'

    with open(file_path,"w") as f:
        json.dump(data,f,indent=4)

    print("Data Loaded")

else:
    print("Data not loaded",response.status_code)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.option("multiline","true").json("Files/Covid_bronze.json")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
