import logging
from logging.handlers import RotatingFileHandler
from kafka import KafkaProducer
from kafka.errors import KafkaError
from tweepy import Stream
import os


class TwitterProducer:
    def __init__(self):
        log_handler = RotatingFileHandler(
            f"{os.path.abspath(os.getcwd())}/kafka/twitter_producer/logs/producer.log",
            maxBytes=104857600, backupCount=10)
        logging.basicConfig(
            format='%(asctime)s,%(msecs)d <%(name)s>[%(levelname)s]: %(message)s',
            datefmt='%H:%M:%S',
            level=logging.DEBUG,
            handlers=[log_handler])
        self.logger = logging.getLogger('coin_producer')

        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:19092', 'localhost:29092', 'localhost:39092'],
            client_id='coin_producer')
        self.twitter_client = Stream("", "", "", "")

    def message_handler(self, message):
        #  Message from binnance sapi
        try:
            if(len(message.keys()) == 11):
                trade_info = f"{message['s']},{message['p']},{message['q']},{message['T']}"
                self.producer.send('coinTradeData', bytes(trade_info, encoding='utf-8'))
                self.producer.flush()
        except KafkaError as e:
            self.logger.error(f"An Kafka error happened: {e}")
        except Exception as e:
            self.logger.error(f"An error happened while pushing message to Kafka: {e}")

    def run(self):
        try:
            with open(os.path.abspath(os.getcwd()) + "/kafka/coin_producer/coin_list.csv") as f:
                coin_list = f.read().split('\n')
            twitter_filter = '$' + ',$'.join(coin_list)
            # print(twitter_filter)
            result = self.twitter_client.filter()
            print(result)
            # self.logger.info("Start running coin producer...")
            # self.ws_client.start()
            # for idx, coin in enumerate(coin_list):
            #     self.ws_client.trade(coin, idx + 1, self.message_handler)
            # # self.ws_client.trade('btcusdt', 1, self.message_handler)
            # while True:
            #     pass
        except Exception as e:
            self.logger.error(f"An error happened while streaming: {e}")
        finally:
            self.twitter_client.disconnect()
