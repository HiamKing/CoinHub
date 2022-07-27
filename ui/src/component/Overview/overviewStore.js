import { action, makeObservable, observable } from "mobx";
import _ from "lodash";
import APIS from "../../services/common";

class OverviewStore {
    curTrendingSymbols = [];
    latestTweets = [];
    symbolChartOptions = {
        title: "Top 10 Symbols has most tweets on Twitter in last 10 minutes",
        width: 600,
        height: 800,
        bar: { groupWidth: "50%" },
        legend: { position: "none" },
    };

    constructor() {
        makeObservable(this, {
            curTrendingSymbols: observable,
            latestTweets: observable,
            fetchOverviewInfo: action,
        });
    }

    fetchOverviewInfo() {
        let trendingSymbols = [[
            "Symbol",
            "Tweet Count",
            { role: "style" },
            {
                sourceColumn: 0,
                role: "annotation",
                type: "string",
                calc: "stringify",
            },
        ]];
        APIS.getOverviewInfo().then((res) => {
            trendingSymbols = trendingSymbols.concat(_.map(res.data.symbols, (symbol) => [
                symbol.symbol.toUpperCase(),
                symbol.tweet_count,
                symbol.color,
                null
            ]));
            this.curTrendingSymbols = trendingSymbols
            this.latestTweets = res.data.tweets;
        });
    }
}

export default new OverviewStore();
