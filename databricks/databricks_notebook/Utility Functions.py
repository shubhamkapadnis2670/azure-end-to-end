# Databricks notebook source
def f_get_secrets(key):
    try:
        return dbutils.secrets.get(scope= 'secret_scope', key= key)
    except Exception as err:
        print(f"Error occured: {err}")

# COMMAND ----------

