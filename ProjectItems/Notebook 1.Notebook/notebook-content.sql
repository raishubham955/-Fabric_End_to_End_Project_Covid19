-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "sqldatawarehouse"
-- META   },
-- META   "dependencies": {
-- META     "warehouse": {
-- META       "default_warehouse": "5fa60f81-705c-ba1a-4626-1f582543096a",
-- META       "known_warehouses": [
-- META         {
-- META           "id": "5fa60f81-705c-ba1a-4626-1f582543096a",
-- META           "type": "Datawarehouse"
-- META         }
-- META       ]
-- META     }
-- META   }
-- META }

-- CELL ********************

-- Query data directly from Lakehouse table (three-part naming)
SELECT * FROM Demo.dbo.covid_silver;


-- METADATA ********************

-- META {
-- META   "language": "sql",
-- META   "language_group": "sqldatawarehouse"
-- META }

-- CELL ********************

-- Create a view in Warehouse referencing Lakehouse data
CREATE VIEW dbo.covid_silver_view AS
SELECT * FROM Demo.dbo.covid_silver;


-- METADATA ********************

-- META {
-- META   "language": "sql",
-- META   "language_group": "sqldatawarehouse"
-- META }
