from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class CoinData(Model):
    symbol = columns.Text(primary_key=True)
    recorded_time = columns.BigInt(primary_key=True, clustering_order="DESC")
    frequency = columns.Text()
    high = columns.Double()
    low = columns.Double()
    open = columns.Double()
    close = columns.Double()
    volume = columns.Double()
