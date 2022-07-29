import { action, makeObservable, observable } from "mobx";
import _ from "lodash";
import APIS from "../../services/common";

class TopTrendStore {
    curTrendingSymbols = [];
    symbolChartCellColor = [];
    latestTweets = [];
    isLoading = false;
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
            symbolChartCellColor: observable,
            latestTweets: observable,
            isLoading: observable,
            fetchOverviewInfo: action,
        });
    }

    fetchOverviewInfo() {
        this.isLoading = true;
        APIS.getOverviewInfo().then((res) => {
            this.curTrendingSymbols = _.map(res.data.symbols, (symbol) => ({
                "symbol": symbol.symbol.toUpperCase(),
                "tweet_count": symbol.tweet_count,
            }));
            this.symbolChartCellColor = _.map(
                res.data.symbols,
                (symbol) => symbol.color
            );
            this.latestTweets = res.data.tweets;
            this.isLoading = false;
        });
    }
}

export default new TopTrendStore();
