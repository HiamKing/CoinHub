import os
from pyspark.sql import SparkSession

os.environ['HADOOP_CONF_DIR'] = os.path.abspath(os.getcwd()) + '/spark/conf'
os.environ['YARN_CONF_DIR'] = os.path.abspath(os.getcwd()) + '/spark/conf'


class CoinTradeDataAnalyzer():
    def __init__(self):
        self.spark = SparkSession.builder\
                                 .config("spark.app.name", "CoinTradeDataAnalyzer")\
                                 .config("spark.jars.packages", "com.datastax.spark:spark-cassandra-connector_2.11:2.5.2")\
                                 .config("spark.cassandra.connection.host", "172.20.0.15")\
                                 .config("spark.cassandra.auth.username", "cassandra")\
                                 .config("spark.cassandra.auth.password", "cassandra")\
                                 .config("spark.master", "yarn")\
                                 .config("spark.driver.memory", "2g")\
                                 .config("spark.executor.memory", "2g")\
                                 .config("spark.executor.instances", "2")\
                                 .getOrCreate()

    def run(self):
        abc = self.spark.read\
            .format("csv")\
            .option("header", True)\
            .option("inferSchema", True)\
            .load("/coinTradeData/2022/7/23/coinTradeData.1658593325")
        abc.printSchema()
        abc.show()


ds = CoinTradeDataAnalyzer()
ds.run()
