secret_value = dbutils.secrets.get(scope="kv-integration-scope", key="dev-secret")
# print(secret_value)
url=f"https://login.microsoftonline.com/{secret_value}/oauth2/token"

configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "5e7778f5-768d-4432-a4d0-ed6dcfd44496",
"fs.azure.account.oauth2.client.secret": 'uM-8Q~WCdSItjOBBgUiqf1ewfy_34sBi9Zd.8bSO',
"fs.azure.account.oauth2.client.endpoint": url}


dbutils.fs.mount(
source = "abfss://raw-data@azurepracticestoragenew.dfs.core.windows.net", # contrainer@storageacc
mount_point = "/mnt/tokyoolymicdata",
extra_configs = configs)

# %fs
# ls "/mnt/tokyoolymicdata"

from pyspark.sql import SparkSession
from pyspark.sql import functions as f
spark=SparkSession.builder.appName('TokyoOlympic').getOrCreate()
schema="Discipline string,Female int, Male int, total int"
Medals_schema="Rank int,TeamCountry string,Gold int,Silver int,Bronze int,Total int,RankbyTotal int"
Athletes=spark.read.format('parquet').load('dbfs:/mnt/tokyoolymicdata/Athletes.parquet')
Coaches=spark.read.format("parquet").load('dbfs:/mnt/tokyoolymicdata/Coaches.parquet')
EntriesGender=spark.read.format("parquet").load('dbfs:/mnt/tokyoolymicdata/EntriesGender.parquet')
Medals=spark.read.format("parquet").load('dbfs:/mnt/tokyoolymicdata/Medals.parquet')
Teams=spark.read.format("parquet").load('dbfs:/mnt/tokyoolymicdata/Teams.parquet')

Athletes.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymicdata/transformed-data/Athletes")
Coaches.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymicdata/transformed-data/Coaches")
EntriesGender.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymicdata/transformed-data/EntriesGender")
Medals.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymicdata/transformed-data/Medals")
Teams.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymicdata/transformed-data/Teams")