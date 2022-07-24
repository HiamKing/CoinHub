from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class TweetTrending(Model):
    symbol = columns.Text(primary_key=True)
    recorded_time = columns.BigInt(primary_key=True, clustering_order="DESC")
    frequency = columns.Text()
    count = columns.Integer()
    sentiment = columns.Integer()

