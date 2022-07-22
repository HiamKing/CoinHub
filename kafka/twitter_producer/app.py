from producer import TwitterProducer


def run_service():
    producer = TwitterProducer()
    producer.run()


run_service()
