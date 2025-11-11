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

# Load Silver data (replace table name if different)
silver_df = spark.read.table("covid_silver")

display(silver_df.limit(5))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

global_df = silver_df.agg(
    F.sum("cases").alias("total_cases"),
    F.sum("deaths").alias("total_death"),
    F.sum("recovered").alias("total_recovered"),
    F.sum("tests").alias("total_case"),
    F.avg("death_rate_pct").alias("avg_death_rate_pct"),
    F.avg("test_per_thousand").alias("avg_test_per_thousand")
)

display(global_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Cell 3 – Top 10 Countries by Cases


# CELL ********************

top_cases_df = (
    silver_df
    .select("country","cases","deaths","death_rate_pct")
    .orderBy(F.col("cases").desc())
    .limit(10)
)

display(top_cases_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

top_cases_df = (
    silver_df
    .select()
    .orderBy(F.col().desc())
    .limit(10)
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Cell 4 – Top 10 Countries by Death Rate


# CELL ********************

top_death_rate_df  = ( silver_df 
    .select("Country","cases","deaths","death_rate_pct")
    .filter("cases > 10000")
    .orderBy(F.col("death_rate_pct").desc())
    .limit(10)
)

display(top_death_rate_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(silver_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# save the gold data Contry level KPIs

gold_df = silver_df.select(
    "country",
    "cases",
    "deaths",
    "recovered",
    "tests",
    "population",
    "death_rate_pct",
    "test_per_thousand",
    "cases_per_million"
)

gold_df.write.mode("overwrite").saveAsTable("Covid_Gold")

print("Gold layer table created")





# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
