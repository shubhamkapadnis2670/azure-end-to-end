# Databricks notebook source
# MAGIC %run "/Workspace/Users/shubhamkapadnis1997@gmail.com/Utility Functions"

# COMMAND ----------

storage_account_name = "csadlsgen2dev"
container_name = "landing"
mount_point = "/mnt/landing"

# Set your client ID, client secret, directory ID, and tenant ID for Service Principal authentication
client_id = f_get_secrets(key='spn-client-id')
client_secret = f_get_secrets(key='spn-client-secret')
directory_id = f_get_secrets(key='spn-tenant-id')


# Define the credentials dictionary
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": client_id,
    "fs.azure.account.oauth2.client.secret": client_secret,
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/token",
    "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

# Mount the ADLS Gen2 filesystem
try:
    dbutils.fs.mount(
        source=f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point=mount_point,
        extra_configs=configs
    )
    print(f"ADLS Gen2 container: {container_name} mounted successfully!")
except Exception as e:
    print(f"Failed to mount ADLS Gen2: {str(e)}")

# COMMAND ----------

storage_account_name = "csadlsgen2dev"
container_name = "bronze"
mount_point = "/mnt/bronze"

# Set your client ID, client secret, directory ID, and tenant ID for Service Principal authentication
client_id = f_get_secrets(key='spn-client-id')
client_secret = f_get_secrets(key='spn-client-secret')
directory_id = f_get_secrets(key='spn-tenant-id')


# Define the credentials dictionary
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": client_id,
    "fs.azure.account.oauth2.client.secret": client_secret,
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/token",
    "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

# Mount the ADLS Gen2 filesystem
try:
    dbutils.fs.mount(
        source=f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point=mount_point,
        extra_configs=configs
    )
    print(f"ADLS Gen2 container: {container_name} mounted successfully!")
except Exception as e:
    print(f"Failed to mount ADLS Gen2: {str(e)}")

# COMMAND ----------

storage_account_name = "csadlsgen2dev"
container_name = "silver"
mount_point = "/mnt/silver"

# Set your client ID, client secret, directory ID, and tenant ID for Service Principal authentication
client_id = f_get_secrets(key='spn-client-id')
client_secret = f_get_secrets(key='spn-client-secret')
directory_id = f_get_secrets(key='spn-tenant-id')


# Define the credentials dictionary
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": client_id,
    "fs.azure.account.oauth2.client.secret": client_secret,
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/token",
    "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

# Mount the ADLS Gen2 filesystem
try:
    dbutils.fs.mount(
        source=f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point=mount_point,
        extra_configs=configs
    )
    print(f"ADLS Gen2 container: {container_name} mounted successfully!")
except Exception as e:
    print(f"Failed to mount ADLS Gen2: {str(e)}")

# COMMAND ----------

storage_account_name = "csadlsgen2dev"
container_name = "gold"
mount_point = "/mnt/gold"

# Set your client ID, client secret, directory ID, and tenant ID for Service Principal authentication
client_id = f_get_secrets(key='spn-client-id')
client_secret = f_get_secrets(key='spn-client-secret')
directory_id = f_get_secrets(key='spn-tenant-id')


# Define the credentials dictionary
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": client_id,
    "fs.azure.account.oauth2.client.secret": client_secret,
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/token",
    "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

# Mount the ADLS Gen2 filesystem
try:
    dbutils.fs.mount(
        source=f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point=mount_point,
        extra_configs=configs
    )
    print(f"ADLS Gen2 container: {container_name} mounted successfully!")
except Exception as e:
    print(f"Failed to mount ADLS Gen2: {str(e)}")

# COMMAND ----------

storage_account_name = "csadlsgen2dev"
container_name = "log"
mount_point = "/mnt/log"

# Set your client ID, client secret, directory ID, and tenant ID for Service Principal authentication
client_id = f_get_secrets(key='spn-client-id')
client_secret = f_get_secrets(key='spn-client-secret')
directory_id = f_get_secrets(key='spn-tenant-id')


# Define the credentials dictionary
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": client_id,
    "fs.azure.account.oauth2.client.secret": client_secret,
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/token",
    "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

# Mount the ADLS Gen2 filesystem
try:
    dbutils.fs.mount(
        source=f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point=mount_point,
        extra_configs=configs
    )
    print(f"ADLS Gen2 container: {container_name} mounted successfully!")
except Exception as e:
    print(f"Failed to mount ADLS Gen2: {str(e)}")

# COMMAND ----------

storage_account_name = "csadlsgen2dev"
container_name = "metadata"
mount_point = "/mnt/metadata"

# Set your client ID, client secret, directory ID, and tenant ID for Service Principal authentication
client_id = f_get_secrets(key='spn-client-id')
client_secret = f_get_secrets(key='spn-client-secret')
directory_id = f_get_secrets(key='spn-tenant-id')


# Define the credentials dictionary
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": client_id,
    "fs.azure.account.oauth2.client.secret": client_secret,
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/token",
    "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

# Mount the ADLS Gen2 filesystem
try:
    dbutils.fs.mount(
        source=f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point=mount_point,
        extra_configs=configs
    )
    print(f"ADLS Gen2 container: {container_name} mounted successfully!")
except Exception as e:
    print(f"Failed to mount ADLS Gen2: {str(e)}")

# COMMAND ----------

storage_account_name = "csadlsgen2devsource"
container_name = "landing"
mount_point = "/mnt/landing_source"

# Set your client ID, client secret, directory ID, and tenant ID for Service Principal authentication
client_id = f_get_secrets(key='spn-client-id')
client_secret = f_get_secrets(key='spn-client-secret')
directory_id = f_get_secrets(key='spn-tenant-id')


# Define the credentials dictionary
configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": client_id,
    "fs.azure.account.oauth2.client.secret": client_secret,
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/token",
    "fs.azure.createRemoteFileSystemDuringInitialization": "true"
}

# Mount the ADLS Gen2 filesystem
try:
    dbutils.fs.mount(
        source=f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point=mount_point,
        extra_configs=configs
    )
    print(f"ADLS Gen2 container: {container_name} mounted successfully!")
except Exception as e:
    print(f"Failed to mount ADLS Gen2: {str(e)}")

# COMMAND ----------

