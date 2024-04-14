# Databricks notebook source
dbutils.widgets.text("env", "")
env = dbutils.widgets.get("env")

dbutils.widgets.text("logic_app_url", "")
logic_app_url = dbutils.widgets.get("logic_app_url")

dbutils.widgets.text("email_id", "")
email_id = dbutils.widgets.get("email_id")

dbutils.widgets.text("storage_account", "")
storage_account = dbutils.widgets.get("storage_account")

dbutils.widgets.text("adls_url", "")
adls_url = dbutils.widgets.get("adls_url")

# COMMAND ----------

#job_id 101
spark.sql(f"""
          
insert into metadata_schema.tbl_source_control values ('sftp_host',101,'{storage_account}','{adls_url}','landing','{logic_app_url}','{email_id}')        
""")

# COMMAND ----------

#job_id 101
spark.sql(f"""

insert into metadata_schema.tbl_parameters values 
(101,'fmcg_fact_transport_diesel.csv','/sftp_files','sftp_flatfiles','{env}_bronze','fact_transport_diesel','{env}_silver','fact_transport_diesel','{env}_gold','fact_transport'),
(101,'fmcg_fact_transport_electric.csv','/sftp_files','sftp_flatfiles','{env}_bronze','fact_transport_electric','{env}_silver','fact_transport_electric','{env}_gold','fact_transport'),
(101,'fmcg_fact_transport_others.csv','/sftp_files','sftp_flatfiles','{env}_bronze','fact_transport_others','{env}_silver','fact_transport_others','{env}_gold','fact_transport'),
(101,'fmcg_fact_transport_petrol.csv','/sftp_files','sftp_flatfiles','{env}_bronze','fact_transport_petrol','{env}_silver','fact_transport_petrol','{env}_gold','fact_transport')
""")

# COMMAND ----------

