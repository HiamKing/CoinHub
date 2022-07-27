import { action, makeObservable, observable } from "mobx";
import APIS from "../../services/common";

class AppStore {
    currentTab = "Overview";

    constructor() {
        makeObservable(this, {
            currentTab: observable,
			changeCurrentTab: action
        });
    }

    changeCurrentTab(tab) {
		this.currentTab = tab
	}
}

export default new AppStore();
