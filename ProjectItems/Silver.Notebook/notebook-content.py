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

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

bronze_df = spark.read.option("multiline","true").json("Files/Covid_bronze.json")

display(bronze_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Flatten nested fields from 'CountryInfo'

silver_df = (
    bronze_df
    .withColumn("country_id" , F.col("countryInfo._id"))
    .withColumn("iso2" , F.col("countryInfo.iso2"))
    .withColumn("iso3" , F.col("countryInfo.iso3"))
    .withColumn("latitude" , F.col("countryInfo.lat"))
    .withColumn("longitude" , F.col("countryInfo.long"))
    .withColumn("flag_url" ,  F.col("countryInfo.flag"))
    .drop("countryInfo")
)

display(silver_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

silver_df = (
    silver_df
    .withColumn("death_rate_pct", F.round((F.col("deaths") / F.col("cases")) * 100 , 2))
    .withColumn("recovery_rate_pct" , F.round((F.col("recovered") / F.col("cases")) * 100, 2))
    .withColumn("active_rate_pct" , F.round((F.col("active") / F.col("cases")) * 100 , 2 ))
    .withColumn("test_per_thousand", F.round((F.col("tests") / F.col("population")) * 100 , 2 ))
    .withColumn("cases_per_million", F.round(F.col("casesPerOneMillion"), 2 ))
)

silver_df = silver_df.na.drop(subset=["cases","deaths","recovered","population"])

display(silver_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

silver_table = "Covid_Silver"
silver_df.write.mode("overwrite").saveAsTable(silver_table)

print(f"Silver table {silver_table} created successfully")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
