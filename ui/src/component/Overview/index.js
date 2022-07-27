import React from "react";
import { observer } from "mobx-react";
import { toJS } from "mobx";
import { Chart } from "react-google-charts";
import overviewStore from "./overviewStore";
import { Default } from "react-awesome-spinners";
import "./styles.css";

class Overview extends React.Component {
    componentDidMount() {
        overviewStore.fetchOverviewInfo();
    }

    getLatestTweet() {
        const store = overviewStore;
        return (
            <div className="tweet-table">
                <div className="tweet-group">
                    <div className="tweet-value">
                        <b>Latest tweets on Twitter</b>
                    </div>
                </div>
                {store.latestTweets.map((tweet) => (
                    <div className="tweet-group">
                        <div className="tweet-value">
                            {tweet.content}
                        </div>
                    </div>
                ))}
            </div>
        );
    }

    render() {
        const store = overviewStore;
        const symbolChartData = toJS(store.curTrendingSymbols)
        
        return (
            <div className="overview">
                <Chart
                    chartType="BarChart"
                    width="100%"
                    height="800px"
                    data={symbolChartData}
                    options={store.symbolChartOptions}
                />
                {this.getLatestTweet()}
            </div>
        );
    }
}

export default observer(Overview);
