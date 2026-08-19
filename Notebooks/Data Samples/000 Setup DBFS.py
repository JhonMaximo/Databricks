# Databricks notebook source
# MAGIC %md
# MAGIC ### Este notebook foi adaptado para Databricks Free Edition
# MAGIC Novo Padrão de Organização
# MAGIC
# MAGIC **Catálogo**: workspace
# MAGIC
# MAGIC **Schema**: lhdw
# MAGIC
# MAGIC **Volumes**: landingzone, bronze, silver, gold
# MAGIC
# MAGIC **Estrutura de pastas:**
# MAGIC /Volumes/workspace/lhdw/landingzone/vendas/processar
# MAGIC
# MAGIC /Volumes/workspace/lhdw/landingzone/vendas/processado
# MAGIC
# MAGIC /Volumes/workspace/lhdw/bronze
# MAGIC
# MAGIC /Volumes/workspace/lhdw/silver
# MAGIC
# MAGIC /Volumes/workspace/lhdw/gold
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Criar os diretórios (DBFS)

# COMMAND ----------

# Criar uma pasta no Databricks para vinculo
#Criando um Schema 
spark.sql("CREATE SCHEMA IF NOT EXISTS workspace.lhdw COMMENT 'Schema LHDW'") 
# Create volumes in Databricks 
spark.sql("CREATE VOLUME IF NOT EXISTS workspace.lhdw.landingzone COMMENT 'Landing zone volume'") 
spark.sql("CREATE VOLUME IF NOT EXISTS workspace.lhdw.bronze COMMENT 'Bronze volume'") 
spark.sql("CREATE VOLUME IF NOT EXISTS workspace.lhdw.silver COMMENT 'Silver volume'") 
spark.sql("CREATE VOLUME IF NOT EXISTS workspace.lhdw.gold COMMENT 'Gold volume'")
 
# Criar uma pasta no Databricks para vinculo # Criando diretorios no DBFS 
dbutils.fs.mkdirs("dbfs:/Volumes/workspace/lhdw/landingzone/vendas/processar") 
dbutils.fs.mkdirs("dbfs:/Volumes/workspace/lhdw/landingzone/vendas/processado") 
dbutils.fs.mkdirs("dbfs:/Volumes/workspace/lhdw/bronze") 
dbutils.fs.mkdirs("dbfs:/Volumes/workspace/lhdw/silver") 
dbutils.fs.mkdirs("dbfs:/Volumes/workspace/lhdw/gold")

# COMMAND ----------

# MAGIC %md
# MAGIC ###Resumo das Diferenças
# MAGIC #####Criar um Diretório: 
# MAGIC   Simplesmente cria uma nova pasta no DBFS para organizar seus dados internos.
# MAGIC
# MAGIC #####Montar um Diretório: 
# MAGIC Conecta um armazenamento de objetos externo ao DBFS, permitindo acesso e manipulação de dados externos como se estivessem localmente no Databricks.
# MAGIC
# MAGIC Documentação de apoio
# MAGIC
# MAGIC https://learn.microsoft.com/pt-br/azure/databricks/files/#work-with-files-in-dbfs-mounts-and-dbfs-root

# COMMAND ----------

# MAGIC %md
# MAGIC Listando os volume criados em database 

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW VOLUMES

# COMMAND ----------

# MAGIC %md
# MAGIC ### Listando todos os Schemas no Workspace

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS IN workspace;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Lista Tabelas de um Schema

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN workspace.lhdw;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Conhecendo os diretórios (DBFS)

# COMMAND ----------

# MAGIC %fs ls 

# COMMAND ----------

# MAGIC %md
# MAGIC ### Conhecendo os diretórios Volumes (DBFS)

# COMMAND ----------

display(
     dbutils.fs.ls(
       "/Volumes/workspace/lhdw/landingzone/"
     )
   )
   # Troque para outros caminhos para explorar

# COMMAND ----------

# MAGIC %md
# MAGIC ### Listando diretorio com retorno em Texto

# COMMAND ----------

dbutils.fs.ls("/Volumes/workspace/lhdw/landingzone/")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Conhecendo os diretórios Volumes/workspace/lhdw (DBFS)

# COMMAND ----------

display(
  dbutils.fs.ls(
    "/Volumes/workspace/lhdw/landingzone"
  )
)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Conhecendo os diretórios /databricks-datasets/ (DBFS)

# COMMAND ----------

# MAGIC %fs ls /databricks-datasets//

# COMMAND ----------

# MAGIC %md
# MAGIC ####Conhecendo os diretórios /databricks-datasets/ (DBFS)

# COMMAND ----------

# MAGIC %fs ls /databricks-datasets/

# COMMAND ----------

# MAGIC %md
# MAGIC ###Apagando Schemas e Volumes
# MAGIC Processar apenas se necessario

# COMMAND ----------

# Apagando Volumes
# spark.sql("DROP VOLUME workspace.lhdw.landingzone") 
# spark.sql("DROP VOLUME workspace.lhdw.bronze") 
# spark.sql("DROP VOLUME workspace.lhdw.silver") 
# spark.sql("DROP VOLUME workspace.lhdw.gold")

# Apagando Schema
# spark.sql("DROP SCHEMA  workspace.lhdw") 