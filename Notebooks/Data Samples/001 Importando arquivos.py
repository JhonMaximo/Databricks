# Databricks notebook source
# MAGIC %md
# MAGIC ###Importar arquivos para DBFS Landingzone
# MAGIC
# MAGIC Para baixar um arquivo do GitHub e salvá-lo no Databricks, você pode seguir os passos abaixo:
# MAGIC

# COMMAND ----------

import requests

url = 'https://github.com/andrerosa77/trn-pyspark/raw/main/dados_2012.csv'
dbfs_path = '/Volumes/workspace/lhdw/landingzone/vendas/processar/dados_2012.csv'

response = requests.get(url)
response.raise_for_status()

dbutils.fs.put(
    dbfs_path,
    response.text,
    overwrite=True
)

print(f"Arquivo baixado e salvo em: {dbfs_path}")

# COMMAND ----------

# MAGIC %md
# MAGIC ##Evidência do Arquivo criado

# COMMAND ----------

display(
dbutils.fs.ls("/Volumes/workspace/lhdw/landingzone/vendas/processar")
)


# COMMAND ----------

# MAGIC
# MAGIC %fs ls /Volumes/workspace/lhdw/landingzone/vendas/processar
# MAGIC