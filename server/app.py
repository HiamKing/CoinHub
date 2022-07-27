from datetime import datetime, timedelta
from flask import Flask, request
from flask_cors import CORS
from cassandra.cluster import Cluster

cluster = Cluster(['172.20.0.15'])
session = cluster.connect('coinhub')

app = Flask(__name__)
CORS(app)


@app.route('/get_overview', methods=['GET'])
def get_overview():
    symbol_limit = request.args.get('symbol_limit') or 10
    tweet_limit = request.args.get('tweet_limit') or 10
    start_time = (datetime.utcnow() - timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S.%f%z')
    tweets = session.execute('select recorded_time, content from recent_tweet')
    symbols = session.execute(
        f"select symbol, sum(count) as tweet_count, sum(sentiment) as total_sentiment from stream_tweet_trending where recorded_time >= '{start_time}' group by symbol allow filtering")

    result = {'symbols': [], 'tweets': []}
    for tweet in tweets:
        result['tweets'].append(
            {'recorded_time': tweet.recorded_time,
             'content': tweet.content})
    for symbol in symbols:
        color = "#0000D1"  # blue
        if symbol.total_sentiment > 0:
            color = "#00D100"  # green
        elif symbol.total_sentiment < 0:
            color = "#D10000"  # red
        result['symbols'].append(
            {'symbol': symbol.symbol,
             'tweet_count': symbol.tweet_count,
             'color': color})

    result['tweets'] = sorted(result['tweets'], key=lambda t: t['recorded_time'], reverse=True)[:tweet_limit]
    result['symbols'] = sorted(result['symbols'], key=lambda t: t['tweet_count'], reverse=True)[:symbol_limit]

    return result


if __name__ == "__main__":
    app.run(debug=True)
