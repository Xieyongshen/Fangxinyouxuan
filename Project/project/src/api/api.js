import {
    wxRequest
} from '@/api/wxRequest';

const apiFanxin = 'http://127.0.0.1:8000'
//获取首页当前店铺下的商品
const getShopProduct = (params) => wxRequest(params, apiFanxin + "/api/getShopProduct");
const login = (params) => wxRequest(params, apiFanxin + "/api/login");
export default {
    getShopProduct,
    login
}