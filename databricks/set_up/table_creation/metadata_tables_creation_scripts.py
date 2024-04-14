# Databricks notebook source
dbutils.widgets.text("storage_account_name", "")
storage_account_name = dbutils.widgets.get("storage_account_name")

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists hive_metastore.metadata_schema

# COMMAND ----------

#tbl_source_control metadata table holds the parameters values for various connections
spark.sql(f"""
create or replace table metadata_schema.tbl_source_control (

    source_ref_id string,
    job_id int,
    storage_account string,
    adls_url string,
    container_name string,
    logic_app_url string,
    email_id string
)
location '/mnt/metadata/tbl_source_control'
""")

# COMMAND ----------

# tbl_parameters holds the parameter values of DDL
spark.sql(f"""
create or replace table metadata_schema.tbl_parameters (

    job_id int,
    source_file_or_table_name string,
    source_file_path string,
    adls_file_path string,
    bronze_schema string,
    bronze_tbl string,
    silver_schema string,
    silver_tbl string,
    gold_schema string,
    gold_tbl string
)
location '/mnt/metadata/tbl_parameters'
""")

# COMMAND ----------

