# Databricks notebook source
# MAGIC %md
# MAGIC ####Criando tabelas Delta

# COMMAND ----------

# Caminho da tabela no Volume
nome_tabela = "dim_segmento"
delta_path = f"/Volumes/workspace/lhdw/gold/vendas_delta/{nome_tabela}"

# Ler os dados do Delta
df = spark.read.format("delta").load(delta_path)

# Registrar no catálogo (sem option("path"))
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(f"workspace.lhdw.{nome_tabela}")
# Verifique se a tabela foi criada
spark.sql("SHOW TABLES IN workspace.lhdw").show();

# COMMAND ----------

# Caminho da tabela no Volume
nome_tabela = "dim_categoria"
delta_path = f"/Volumes/workspace/lhdw/gold/vendas_delta/{nome_tabela}"

# Ler os dados do Delta
df = spark.read.format("delta").load(delta_path)

# Registrar no catálogo (sem option("path"))
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(f"workspace.lhdw.{nome_tabela}")
# Verifique se a tabela foi criada
spark.sql("SHOW TABLES IN workspace.lhdw").show();

# COMMAND ----------

# Caminho da tabela no Volume
nome_tabela = "dim_produto"
delta_path = f"/Volumes/workspace/lhdw/gold/vendas_delta/{nome_tabela}"

# Ler os dados do Delta
df = spark.read.format("delta").load(delta_path)

# Registrar no catálogo (sem option("path"))
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(f"workspace.lhdw.{nome_tabela}")
# Verifique se a tabela foi criada
spark.sql("SHOW TABLES IN workspace.lhdw").show();

# COMMAND ----------

# Caminho da tabela no Volume
nome_tabela = "dim_fabricante"
delta_path = f"/Volumes/workspace/lhdw/gold/vendas_delta/{nome_tabela}"

# Ler os dados do Delta
df = spark.read.format("delta").load(delta_path)

# Registrar no catálogo (sem option("path"))
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(f"workspace.lhdw.{nome_tabela}")
# Verifique se a tabela foi criada
spark.sql("SHOW TABLES IN workspace.lhdw").show();

# COMMAND ----------

# Caminho da tabela no Volume
nome_tabela = "dim_geografia"
delta_path = f"/Volumes/workspace/lhdw/gold/vendas_delta/{nome_tabela}"

# Ler os dados do Delta
df = spark.read.format("delta").load(delta_path)

# Registrar no catálogo (sem option("path"))
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(f"workspace.lhdw.{nome_tabela}")
# Verifique se a tabela foi criada
spark.sql("SHOW TABLES IN workspace.lhdw").show();

# COMMAND ----------

# Caminho da tabela no Volume
nome_tabela = "dim_cliente"
delta_path = f"/Volumes/workspace/lhdw/gold/vendas_delta/{nome_tabela}"

# Ler os dados do Delta
df = spark.read.format("delta").load(delta_path)

# Registrar no catálogo (sem option("path"))
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(f"workspace.lhdw.{nome_tabela}")
# Verifique se a tabela foi criada
spark.sql("SHOW TABLES IN workspace.lhdw").show();

# COMMAND ----------

# Caminho da tabela no Volume
nome_tabela = "fato_vendas"
delta_path = f"/Volumes/workspace/lhdw/gold/vendas_delta/{nome_tabela}"

# Ler os dados do Delta
df = spark.read.format("delta").load(delta_path)

# Registrar no catálogo (sem option("path"))
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable(f"workspace.lhdw.{nome_tabela}")
# Verifique se a tabela foi criada
spark.sql("SHOW TABLES IN workspace.lhdw").show();

# COMMAND ----------

import gc
# spark.catalog.clearCache() não compativel com serverless
# Coletar lixo após operações pesadas para liberar memória
gc.collect()

# COMMAND ----------

