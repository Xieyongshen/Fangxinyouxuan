import {
    wxRequest
} from '@/api/wxRequest';

const apiFanxin = 'http://127.0.0.1:8000'
//获取首页店铺商品分类
const getShopCategory = (params) => wxRequest(params, apiFanxin + "/api/getShopCategory");
//获取首页当前店铺下的商品
const getShopProduct = (params) => wxRequest(params, apiFanxin + "/api/getShopProduct");
//登录
const login = (params) => wxRequest(params, apiFanxin + "/api/login");
//获取当前大分类下小分类商品
const getCategoryProduct = (params) => wxRequest(params, apiFanxin + "/api/getCategoryProduct");
//获取商品详情
const getProductDetail = (params) => wxRequest(params, apiFanxin + "/api/getProductDetail");



export default {
    getShopCategory,
    getShopProduct,
    login,
    getCategoryProduct,
    getProductDetail
}