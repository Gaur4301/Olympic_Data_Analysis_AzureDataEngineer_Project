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