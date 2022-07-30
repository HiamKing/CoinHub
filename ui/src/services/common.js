import axios from 'axios';

const API_ROOT = process.env.REACT_APP_API_ROOT || '';

const APIS = {
	getOverviewInfo: () => axios.get(`${API_ROOT}/get_overview`),
	getTrendingSymbols: (args) => axios.get(`${API_ROOT}/get_trending_symbols`, {params: args}),
    getAddress: () => axios.get(`${API_ROOT}/address`),
    getAddressDetail: (address) => axios.get(`${API_ROOT}/address/${address}`),
    sendTransaction: (data) => axios.post(`${API_ROOT}/transaction`, data)
};

export default APIS;
