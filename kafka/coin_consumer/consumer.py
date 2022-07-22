import logging
import os
import tempfile
from logging.handlers import RotatingFileHandler
from kafka import KafkaConsumer
from hdfs import InsecureClient


class CoinConsumer:
    def __init__(self):
        log_handler = RotatingFileHandler(
            f"{os.path.abspath(os.getcwd())}/kafka/coin_consumer/logs/consumer.log",
            maxBytes=104857600, backupCount=10)
        logging.basicConfig(
            format='%(asctime)s,%(msecs)d <%(name)s>[%(levelname)s]: %(message)s',
            datefmt='%H:%M:%S',
            level=logging.DEBUG,
            handlers=[log_handler])
        self.logger = logging.getLogger('coin_consumer')
        self.consumer = KafkaConsumer(
            'coinTradeData',
            bootstrap_servers=['localhost:19092', 'localhost:29092', 'localhost:39092'],
            group_id='tradeDataConsummers',
            auto_offset_reset='earliest',
            enable_auto_commit=False)
        self.hdfs_client = InsecureClient('http://localhost:9870', user='root')

    def flush_to_hdfs(tmp_file_name):
        pass

    def run(self):
        try:
            # tmp_file = tempfile.TemporaryFile()
            # tmp_file.write('Symbol,Price,Quantity,Trade time\n')
            self.logger.info("Subcribe to topic coinTradeData")
            while True:
                msgs_pack = self.consumer.poll(10.0)
                if msgs_pack is None:
                    continue

                for tp, messages in msgs_pack.items():
                    for message in messages:
                        print(message)
                    # tmp_file.write(f"{msg['value']}\n")

                # File size > 100mb flush to hdfs
                # if tmp_file.tell() > 104857600:
                #     fluh_to_hdfs(tmp_file.name)
                #     tmp_file.close()
                #     tmp_file = tempfile.TemporaryFile()
                #     self.consumer.commit()

            # new_path = self.hdfs_client.upload('/', '/home/hiamking/Projects/DE/Project_II/CoinHub/kafka/coin_consumer/app.py')
            # print(new_path)
            # content = self.hdfs_client.list('/')
            # print(content)
        except Exception as e:
            self.logger.error(
                f"An error happened while consuming messages from kafka: {e}")
        finally:
            self.consumer.close()


abc = CoinConsumer()
abc.run()