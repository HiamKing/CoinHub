import React from "react";
import { observer } from "mobx-react";
import { toJS } from "mobx";
import { Default } from "react-awesome-spinners";
import _ from "lodash";
import {
    BarChart,
    CartesianGrid,
    XAxis,
    YAxis,
    Tooltip,
    Bar,
    Cell,
} from "recharts";
import "./styles.css";
import topTrendStore from "./topTrendStore";

class TopTrending extends React.Component {
    render() {
        const store = topTrendStore;
        const symbolChartData = toJS(store.curTrendingSymbols);

        return (
            <div className="overview">
                <div className="chart-view">
                    <BarChart
                        width={600}
                        layout="vertical"
                        height={600}
                        margin={{ top: 40, right: 40, left: 40, bottom: 40 }}
                        data={symbolChartData}
                    >
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis type="number" />
                        <YAxis type="category" dataKey="symbol" />
                        <Tooltip content={this.customTooltip} />
                        <Bar dataKey="tweet_count" maxBarSize={30} fill="#5C5CFF">
                            {this.getSymbolChartCell()}
                        </Bar>
                    </BarChart>
                </div>
                {this.getLatestTweet()}
            </div>
        );
    }
}

export default observer(TopTrending);
