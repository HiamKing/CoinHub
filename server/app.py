from datetime import datetime, timedelta
from flask import Flask, request
from cassandra.cluster import Cluster

cluster = Cluster(['172.20.0.15'])
session = cluster.connect('coinhub')

app = Flask(__name__)


@app.route('/get_tweet', methods=['GET'])
def get_tweet():
    limit = request.args.get('limit') or 20
    tweet_trending = session.execute('select recorded_time, content from recent_tweet')
    result = {'tweet': []}
    for tweet in tweet_trending:
        result['tweet'].append(
            {'recorded_time': tweet.recorded_time,
             'content': tweet.content})
    result['tweet'] = sorted(result['tweet'], key=lambda t: t['recorded_time'], reverse=True)[:limit]
    return result


@app.route('/get_symbol_trending', methods=['GET'])
def get_symbol_trending():
    frequency = request.args.get('frequency') or 10
    start_time = (datetime.utcnow() - timedelta(minutes=frequency)).strftime('%Y-%m-%d %H:%M:%S.%f%z')
    tweet_trending = session.execute(
        f"select symbol, sum(count) as tweet_count, sentiment from tweet_trending where recorded_time >= '2022-07-24 14:30:00.000000' group by symbol allow filtering")
    result = {'tweet_trending': []}
    for tweet in tweet_trending:
        color = 'blue'
        if tweet.sentiment > 0:
            color = 'green'
        elif tweet.sentiment < 0:
            color = 'red'
        result['tweet_trending'].append(
            {'symbol': tweet.symbol,
             'tweet_count': tweet.tweet_count,
             'color': color})

    return result


if __name__ == "__main__":
    app.run(debug=True)
